document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".button, .nav-link, .text-link");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            button.animate(
                [
                    { transform: "translateY(0) scale(1)" },
                    { transform: "translateY(-2px) scale(0.98)" },
                    { transform: "translateY(0) scale(1)" },
                ],
                { duration: 220, easing: "ease-out" }
            );
        });
    });

    const form = document.querySelector(".contact-form");

    if (form) {
        form.addEventListener("submit", (event) => {
            event.preventDefault();
            const submitButton = form.querySelector("button[type='submit']");

            if (submitButton) {
                submitButton.textContent = "Message Ready";
            }
        });
    }

    const sequenceText = document.querySelector(".js-sequence-text");

    if (sequenceText) {
        const messages = [sequenceText.dataset.messageOne, sequenceText.dataset.messageTwo].filter(Boolean);
        const pauseMs = 900;
        const typeDelayMs = 45;
        let messageIndex = 0;

        const sleep = (duration) => new Promise((resolve) => window.setTimeout(resolve, duration));

        const typeMessage = async (message) => {
            sequenceText.textContent = "";

            for (const character of message) {
                sequenceText.textContent += character;
                await sleep(typeDelayMs);
            }

            await sleep(pauseMs);
        };

        const runSequence = async () => {
            while (messages.length > 0) {
                await typeMessage(messages[messageIndex]);
                messageIndex = (messageIndex + 1) % messages.length;
            }
        };

        runSequence();
    }
});