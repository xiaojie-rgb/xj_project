# from flask_mysqldb import MySQL
import time

from flask import Flask, template_rendered, request, redirect, url_for, render_template, session, flash, jsonify
from api_code.search_job import handle_job_data  # 导入函数
from api_code.resume_analysis import resume
from api_code.upload_file import upload
from api_code.interview import handle_interview
from api_code.interview_results import interview_re
import math
import markdown
import bleach
from models import db, User

app = Flask(__name__)

app.config.from_pyfile('settings.py')
# mysql = MySQL(app)
db.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or '@' not in email:
            flash('请输入有效的邮箱地址', 'danger')
            return render_template('login.html', email=email)

        if not password:
            flash('请输入密码', 'danger')
            return render_template('login.html', email=email)

        user = db.session.query(User).filter_by(email=email).first()
        try:
            if user and user.check_password(password):
                session['user_id'] = user.id
                session['user_name'] = user.name
                flash('登录成功,即将跳转到首页!', 'success')
                return render_template('login.html')
            else:
                flash('邮箱或密码错误!', 'danger')
        except Exception as e:
            db.session.rollback()
            flash('登录失败，请稍后再试', 'danger')
            app.logger.error(f'登录错误: {str(e)}')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirmPassword', '')

        errors = []

        # 验证逻辑
        if not name:
            errors.append('姓名不能为空')
        if not email or '@' not in email:
            errors.append('请输入有效的邮箱地址')
        if len(password) < 6:
            errors.append('密码长度至少6位')
        if password != confirm_password:
            errors.append('两次输入的密码不一致')

        if errors:
            for error in errors:
                flash(error, 'danger')
                return render_template('register.html', name=name, email=email)
        try:
            if User.query.filter_by(email=email).first():
                flash('该邮箱已被注册', 'danger')
                return render_template('register.html', name=name, email=email)
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash('注册成功！请登录', 'success')

        except Exception as e:
            db.session.rollback()
            flash('注册失败，请稍后再试', 'danger')
            app.logger.error(f'注册错误: {str(e)}')

    return render_template('register.html')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/resume_analysis')
def resume_analysis():
    return render_template('resume_analysis.html')


@app.route('/resume_results', methods=['GET', 'POST'])
def resume_results():
    if request.method == 'POST':
        job_name = request.form.get('target_position')
        uploaded_file = request.files.get('resume')
        if uploaded_file:
            file_id = upload(uploaded_file)
            suggestions = resume(job_name, file_id)  # 确保此处是 Markdown 内容

            # Markdown 转 HTML
            html_content = markdown.markdown(suggestions)
            # 允许常见 HTML 标签（根据需求扩展）
            allowed_tags = [
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'br', 'hr',
                'ul', 'ol', 'li', 'strong', 'em', 'a', 'code'
            ]
            cleaned_html = bleach.clean(html_content, tags=allowed_tags)
            return render_template('resume_results.html', suggestions=cleaned_html)
        else:
            return "未收到文件", 400
    else:
        return redirect(url_for('resume_analysis'))


@app.route('/interview', methods=['GET', 'POST'])
def interview():
    if request.method == 'POST':
        file = request.files.get('resume')
        interview_type = request.form.get('type')
        job = request.form.get('job')
        difficulty = request.form.get('difficulty')
        if file:
            try:
                file_id = upload(file)
                question_list = handle_interview(interview_type, job, difficulty, file_id)
                session['question_list'] = question_list  # 存储到会话中
                return redirect(url_for('interview_question'))
            except Exception as e:
                print(f"上传或处理过程中出错: {e}")
                return "上传失败，请稍后再试", 500

    return render_template('interview.html')


@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    user_answers = request.get_json()
    # print("Received answers:", user_answers)  # 控制台输出接收的答案
    session['user_answers'] = user_answers
    # print("Session answers:", session.get('user_answers'))  # 确认存入session
    return jsonify({'status': 'success'})


@app.route('/interview_question')
def interview_question():
    question_list = session.get('question_list', [])  # 获取问题列表
    return render_template('interview_question.html', question_list=question_list)


@app.route('/interview_results')
def interview_result():
    question_list = session.get('question_list', [])  # 获取问题列表
    answers_list = session.get('user_answers', [])  # 获取用户答案
    result = interview_re(
        que1=question_list[0]['content'],  # 第1题内容
        que2=question_list[1]['content'],  # 第2题内容
        que3=question_list[2]['content'],  # 第3题内容
        que4=question_list[3]['content'],  # 第4题内容
        que5=question_list[4]['content'],  # 第5题内容
        ans1=answers_list[0],  # 第1题答案
        ans2=answers_list[1],  # 第2题答案
        ans3=answers_list[2],  # 第3题答案
        ans4=answers_list[3],  # 第4题答案
        ans5=answers_list[4],  # 第5题答案
    )
    # Markdown 转 HTML
    html_content = markdown.markdown(result)
    # 允许常见 HTML 标签（根据需求扩展）
    allowed_tags = [
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'br', 'hr',
        'ul', 'ol', 'li', 'strong', 'em', 'a', 'code','pre'
    ]
    cleaned_html = bleach.clean(html_content, tags=allowed_tags)
    return render_template('interview_results.html', result=cleaned_html)


@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    # 每页显示数量
    per_page = 3

    # 获取当前页码 通过 request.args.get 从 URL 参数（如?page=2）中获取当前页码，默认值为 1，确保类型为整数
    page = request.args.get('page', 1, type=int)

    if request.method == 'POST':
        job_name = request.form.get('job_name')
        city = request.form.get('city')
        education = request.form.get('education')
        salaryMin = request.form.get('salaryMin')
        workExperience = request.form.get('workExperience')

        # 对表单数据进行检查和处理，确保参数有效
        if not job_name:
            flash('请输入岗位名称', 'danger')
            return redirect(url_for('index'))  # 重定向回首页或搜索页面提示用户
        if not city:
            flash('请输入城市', 'danger')
            return redirect(url_for('index'))  # 重定向回首页或搜索页面提示用户
        if not education:
            flash('请输入教育背景', 'danger')
            return redirect(url_for('index'))  # 重定向回首页或搜索页面提示用户
        if not salaryMin:
            flash('请输入最低薪资', 'danger')
            return redirect(url_for('index'))  # 重定向回首页或搜索页面提示用户
        if not workExperience:
            flash('请输入工作经验', 'danger')
            return redirect(url_for('index'))  # 重定向回首页或搜索页面提示用户
        try:
            # 处理表单数据获取职位列表
            jobs = handle_job_data(
                job_name=job_name,
                city=city,
                education=education,
                salaryMin=salaryMin,
                workExperience=workExperience,
            )
            # 搜索结果存入 session，以便在后续的分页请求（GET）中复用，避免重复执行搜索逻辑。
            session['search_results'] = jobs
            # 重定向到GET请求避免重复提交
            return redirect(url_for('search_results', page=1))
        except Exception as e:
            flash('搜索出现错误，请重试', 'danger')
            app.logger.error(f'搜索错误: {str(e)}')
            return redirect(url_for('index'))  # 重定向回首页或搜索页面提示用户

    # 从session获取缓存的搜索结果
    jobs = session.get('search_results', [])

    # 计算分页参数
    total_jobs = len(jobs)  # 总职位数量
    total_pages = math.ceil(total_jobs / per_page) if total_jobs else 1  # 总页数，使用向上取整

    # 确保页码在有效范围（防止用户输入非法页码）
    page = max(1, min(page, total_pages))

    # 分页切片
    start = (page - 1) * per_page
    end = start + per_page
    jobs_page = jobs[start:end]

    # 计算翻页状态
    has_prev = page > 1  # 是否有上一页
    has_next = page < total_pages  # 是否有下一页

    return render_template(
        'search_results.html',
        jobs=jobs_page,
        total_jobs=total_jobs,
        page=page,
        total_pages=total_pages,
        has_prev=has_prev,
        has_next=has_next,
    )


if __name__ == '__main__':
    app.run(debug=True)
