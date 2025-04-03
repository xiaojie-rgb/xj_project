window.onload = function () {
    window.jsPDF = window.jspdf.jsPDF;

    document.getElementById('downloadReportBtn').addEventListener('click', async function () {
        const btn = this;
        let element;
        let originalStyles = {}; // 初始化以在finally中安全使用

        try {
            btn.disabled = true;
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 正在生成PDF...';

            // 强制重绘按钮状态
            await new Promise(resolve => requestAnimationFrame(resolve));

            element = document.querySelector('.analysis-card');
            if (!element) throw new Error('找不到报告内容区域');

            // 保存当前内联样式
            originalStyles = {
                overflow: element.style.overflow,
                width: element.style.width
            };

            // 应用打印优化样式
            element.style.overflow = 'visible';
            element.style.width = '794px';

            // 生成Canvas
            const canvas = await html2canvas(element, {
                scale: 2,
                useCORS: true,
                allowTaint: false
            });

            // 生成PDF
            const pdf = new jsPDF({orientation: 'portrait', unit: 'mm', format: 'a4'});
            const imgHeight = (canvas.height * 210) / canvas.width;
            pdf.addImage(canvas, 'PNG', 0, 0, 210, imgHeight);

            // 添加页脚
            const dateStr = new Date().toLocaleDateString('zh-CN', {year: 'numeric', month: '2-digit', day: '2-digit'});
            pdf.text(`超级面试官 - 生成日期：${dateStr}`, 10, 287);

            pdf.save(`简历分析报告_${dateStr.replace(/\//g, '-')}.pdf`);

        } catch (error) {
            console.error('生成失败:', error);
            alert('生成失败，请重试');
        } finally {
            // 同步恢复元素样式
            if (element) {
                element.style.overflow = originalStyles.overflow || '';
                element.style.width = originalStyles.width || '';
            }

            // 同步恢复按钮状态
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-download"></i> 下载完整报告';
        }
    });
};