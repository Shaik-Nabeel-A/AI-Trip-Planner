async function generatePlan() {
    const promptInput = document.getElementById('prompt');
    const prompt = promptInput.value.trim();
    const resultCard = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');
    const contentDiv = document.getElementById('markdown-content');
    const generateBtn = document.getElementById('generateBtn');

    if (!prompt) return;

    // UI State Updates
    generateBtn.disabled = true;
    generateBtn.style.opacity = '0.7';
    loadingDiv.classList.remove('hidden');
    resultCard.classList.add('hidden');

    // Simulate steps for better UX
    const steps = ['step1', 'step2', 'step3'];
    let stepIndex = 0;
    const stepInterval = setInterval(() => {
        if (stepIndex < steps.length) {
            document.querySelectorAll('.step').forEach(s => s.style.opacity = '0.5');
            document.getElementById(steps[stepIndex]).style.opacity = '1';
            document.getElementById(steps[stepIndex]).style.color = '#6366f1';
            stepIndex++;
        }
    }, 2000);

    try {
        const response = await fetch('/api/plan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();

        clearInterval(stepInterval);

        if (data.error) {
            contentDiv.innerHTML = `<p style="color: #ef4444;">Error: ${data.error}</p>`;
        } else {
            // Parse Markdown
            contentDiv.innerHTML = marked.parse(data.plan);
        }

        resultCard.classList.remove('hidden');

        // Scroll to result
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

    } catch (e) {
        contentDiv.innerHTML = `<p style="color: #ef4444;">Network Error: ${e.message}</p>`;
        resultCard.classList.remove('hidden');
    } finally {
        loadingDiv.classList.add('hidden');
        generateBtn.disabled = false;
        generateBtn.style.opacity = '1';
    }
}

function copyToClipboard() {
    const content = document.getElementById('markdown-content').innerText;
    navigator.clipboard.writeText(content).then(() => {
        const btn = document.querySelector('.copy-btn');
        const originalHTML = btn.innerHTML;
        btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
        setTimeout(() => {
            btn.innerHTML = originalHTML;
        }, 2000);
    });
}
