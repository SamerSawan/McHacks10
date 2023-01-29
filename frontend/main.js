// TEXT ANIMATION

const text = document.querySelector(".first-slide");

const textLoad = () => {
    setTimeout(() => {
        text.textContent = "user sentiment.";
    }, 0);
    setTimeout(() => {
        text.textContent = "worker satisfaction.";
    }, 4100);
    setTimeout(() => {
        text.textContent = "affordable delivery.";
    }, 8100);
}

textLoad();
setInterval(textLoad, 12000);