// ckeditor.code-block.js
// 🎯 Enhances CKEditor-rendered <pre><code> blocks
// 🧩 Adds language label + copy button
// 💡 Used only for frontend rendering, not CKEditor config

import hljs from 'highlight.js/lib/core'

import javascript from 'highlight.js/lib/languages/javascript'
import python from 'highlight.js/lib/languages/python'
import html from 'highlight.js/lib/languages/xml'

// Register only required languages for optimization
hljs.registerLanguage('javascript', javascript)
hljs.registerLanguage('python', python)
hljs.registerLanguage('html', html)

/**
 * Initialize syntax highlighting and UI enhancement for code blocks
 */
export function renderCodeBlocks() {
    hljs.highlightAll();

    document.querySelectorAll('pre code.hljs').forEach(code => {
        const lang = code.className.match(/language-(\w+)/)?.[1] || 'code';
        const pre = code.parentElement;

        const wrapper = document.createElement('div');
        wrapper.className = 'ckeditor code-wrapper code-block-container';
        wrapper.setAttribute('dir', 'ltr');

        const header = document.createElement('div');
        header.className = 'code-wrapper-header';
        header.innerHTML = `
            <span class="text-blue-400 lowercase">${lang}</span>
            <button class="copy-btn text-gray-400 hover:text-white transition cursor-pointer">📋 Copy</button>
        `;

        wrapper.appendChild(header);
        wrapper.appendChild(pre.cloneNode(true));
        pre.replaceWith(wrapper);
    });

    // Copy logic
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const code = btn.closest('.code-wrapper')?.querySelector('code');
            if (!code) return;

            navigator.clipboard.writeText(code.innerText).then(() => {
                const original = btn.innerHTML;
                btn.innerHTML = "✅ Copied";
                btn.classList.add("text-green-400");

                setTimeout(() => {
                    btn.innerHTML = original;
                    btn.classList.remove("text-green-400");
                }, 2000);
            });
        });
    });
}
