window.onload = function () {
    const resumeInput = document.getElementById('resume-input');
    const fileInfo = document.getElementById('file-info');
    const startBtn = document.getElementById('start-btn');
    const loader = document.getElementById('loader');

    // 文件验证函数
    function validateFile(file) {
        const validTypes = [
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ];
        return validTypes.includes(file.type) && file.size <= 10 * 1024 * 1024;
    }

    // 文件上传处理
    resumeInput.addEventListener('change', function (e) {
        const file = e.target.files[0];
        if (file && validateFile(file)) {
            fileInfo.innerHTML = `
                <div style="color: #27ae60; margin-top: 1rem;">
                    <i class="fas fa-check-circle"></i>
                    已上传：${file.name} (${formatSize(file.size)})
                </div>
            `;
            startBtn.disabled = false;
        } else {
            fileInfo.innerHTML = `
                <div style="color: #e74c3c; margin-top: 1rem;">
                    <i class="fas fa-exclamation-triangle"></i>
                    请上传有效的简历文件
                </div>
            `;
            startBtn.disabled = true;
        }
    });

    // 开始面试按钮点击事件
    startBtn.addEventListener('click', function () {
        loader.style.display = 'block';
        startBtn.disabled = true;
        startBtn.innerHTML = '上传中...';

        const file = resumeInput.files[0];
        if (!file || !validateFile(file)) {
            alert('请先选择有效的简历文件');
            loader.style.display = 'none';
            startBtn.disabled = false;
            startBtn.innerHTML = '🚀 开始模拟面试';
            return;
        }

        const formData = new FormData();
        formData.append('resume', file);
        formData.append('type', document.getElementById('interview-type').value);
        formData.append('job', document.getElementById('job-field').value);
        formData.append('difficulty', document.getElementById('difficulty').value);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/interview', true);

        xhr.onload = function () {
            loader.style.display = 'none';
            if (xhr.status === 200) {
                window.location.href = '/interview_question';
            } else {
                alert(`上传失败: ${xhr.responseText}`);
            }
            startBtn.disabled = false;
            startBtn.innerHTML = '🚀 开始模拟面试';
        };

        xhr.onerror = function () {
            loader.style.display = 'none';
            alert('网络连接失败');
            startBtn.disabled = false;
            startBtn.innerHTML = '🚀 开始模拟面试';
        };

        xhr.send(formData);
    });

    // 辅助函数：格式化文件大小
    function formatSize(bytes) {
        const sizes = ['Bytes', 'KB', 'MB'];
        if (bytes === 0) return '0 Byte';
        const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
        return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
    }
};