export function initTocInteraction() {
    const tocLinks = document.querySelectorAll(".toc-list a");
    const sections = Array.from(tocLinks)
        .map(link => document.querySelector(link.getAttribute("href")))
        .filter(Boolean); // Remove nulls in case of bad anchor

    const observerOptions = {
        root: null,
        rootMargin: "0px",
        threshold: 0.3
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocLinks.forEach(link => {
                    link.classList.remove("text-blue-600", "font-semibold");
                    if (link.getAttribute("href") === `#${entry.target.id}`) {
                        link.classList.add("text-blue-600", "font-semibold");
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => observer.observe(section));
}
