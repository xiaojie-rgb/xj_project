window.onload = function () {
    const fileInput = document.getElementById('file-input');
    const positionInput = document.getElementById('target-position');
    const statusDiv = document.getElementById('upload-status');
    const analyzeBtn = document.getElementById('analyze-btn');
    const loader = document.getElementById('loader');

    // 检查表单是否可提交
    function checkForm() {
        const fileValid = fileInput.files.length > 0 && validateFile(fileInput.files[0]);
        const positionValid = positionInput.value.trim().length > 0;
        analyzeBtn.disabled = !(fileValid && positionValid);
    }

    // 文件选择处理
    fileInput.addEventListener('change', function (e) {
        const file = e.target.files[0];
        if (file) {
            if (validateFile(file)) {
                statusDiv.innerHTML = `
                    <div style="color: #27ae60; margin: 1rem 0;">
                        <i class="fas fa-check-circle"></i>
                        已选择文件：${file.name} (${formatFileSize(file.size)})
                    </div>
                `;
            } else {
                statusDiv.innerHTML = `
                    <div style="color: #e74c3c; margin: 1rem 0;">
                        <i class="fas fa-exclamation-triangle"></i>
                        文件格式或大小不符合要求
                    </div>
                `;
            }
        }
        checkForm();
    });

    // 岗位输入变化时检查
    positionInput.addEventListener('input', checkForm);

    // 文件验证
    function validateFile(file) {
        const validTypes = ['application/pdf', 'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
        const maxSize = 10 * 1024 * 1024; // 10MB
        return validTypes.includes(file.type) && file.size <= maxSize;
    }

    // 格式化文件大小
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    // 修改重点：处理表单提交
    analyzeBtn.addEventListener('click', function (e) {
        e.preventDefault(); // 阻止默认提交行为

        const position = positionInput.value.trim();
        const file = fileInput.files[0];

        // 前端验证
        if (!position) {
            alert('请输入目标岗位');
            return;
        }

        if (!file || !validateFile(file)) {
            alert('请选择有效的简历文件');
            return;
        }

        // 显示加载状态
        loader.style.display = 'block';
        analyzeBtn.disabled = true;
        statusDiv.innerHTML += `
            <div style="color: #3498db; margin-top: 1rem;">
                <i class="fas fa-sync-alt fa-spin"></i>
                正在分析【${position}】岗位匹配度...
            </div>
        `;

        // 关键修改：手动触发表单提交
        document.querySelector('form').submit();
    });
}