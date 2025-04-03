let currentQuestionIndex = 0;
let answers = [];
let timer;

window.onload = function () {
    document.getElementById('totalQuestions').textContent = question_list.length;
    answers = new Array(question_list.length).fill(''); // 初始化答案数组
    loadQuestion(0);
    startTimer(question_list.length * 300);
};

function loadQuestion(index) {
    console.log('加载问题，索引:', index);
    currentQuestionIndex = index;
    const question = question_list[index];

    // 更新进度条
    const progressWidth = ((index + 1) / question_list.length) * 100;
    document.getElementById('progressBar').style.width = `${progressWidth}%`;

    // 更新题目信息
    document.getElementById('currentQuestion').textContent = index + 1;
    document.getElementById('questionContent').innerHTML = `
        <h4>${question.title}</h4>
        <div>${question.content}</div>
    `;

    // 更新按钮状态
    document.getElementById('prevBtn').disabled = index === 0;
    document.getElementById('nextBtn').textContent =
        index === question_list.length - 1 ? '提交面试' : '下一题';
}

function prevQuestion() {
    if (currentQuestionIndex > 0) {
        saveAnswer();
        loadQuestion(currentQuestionIndex - 1);
    }
}

function nextQuestion() {
    console.log('点击了下一题按钮');
    if (currentQuestionIndex < question_list.length - 1) {
        console.log('当前问题索引:', currentQuestionIndex);
        saveAnswer();
        loadQuestion(currentQuestionIndex + 1);
    } else {
        console.log('最后一题，提交面试');
        saveAnswer();
        submitInterview();
    }
}

function saveAnswer() {
    answers[currentQuestionIndex] = document.getElementById('userAnswer').value;
    document.getElementById('userAnswer').value = '';
}

function startTimer(totalSeconds) {
    let remaining = totalSeconds;
    timer = setInterval(() => {
        const min = Math.floor(remaining / 60);
        const sec = remaining % 60;
        document.getElementById('timer').textContent =
            `剩余时间：${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;

        if (remaining-- <= 0) {
            clearInterval(timer);
            submitInterview();
        }
    }, 1000);
}

function submitInterview() {
    clearInterval(timer);

    // 显示加载动画
    const loadingOverlay = document.getElementById('loadingOverlay');
    loadingOverlay.style.display = 'flex';

    // 发送答案到后端
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit_answers', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // 直接跳转不再需要隐藏加载动画
                window.location.href = '/interview_results';
            } else {
                // 处理错误情况
                loadingOverlay.style.display = 'none';
                alert('提交失败，请检查网络后重试！');
            }
        }
    };
    const answersData = JSON.stringify(answers);
    xhr.send(answersData);
}


// 暴露函数到全局作用域
window.prevQuestion = prevQuestion;
window.nextQuestion = nextQuestion;