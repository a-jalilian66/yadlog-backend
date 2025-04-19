// js/main.js
import Alpine from 'alpinejs'
import {renderCodeBlocks} from './ckeditor/ckeditor.code-block.js'
import {initTocInteraction} from './interactions/toc-interaction.js'
import './interactions/hover-sounds.js'

window.Alpine = Alpine
Alpine.start()

document.addEventListener('DOMContentLoaded', () => {
    renderCodeBlocks();
    initTocInteraction();
});
