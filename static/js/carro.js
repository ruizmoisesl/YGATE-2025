const carousel = document.getElementById('carousel');
const items = document.querySelectorAll('.carousel-item');
let currentIndex = 0;

function updateCarousel() {
    // Calcula el desplazamiento en función del índice actual
    const offset = -currentIndex * items[0].offsetWidth;
    carousel.style.transform = `translateX(${offset}px)`;
}

function nextItem() {
    // Avanza al siguiente elemento, o vuelve al primero si está al final
    currentIndex = (currentIndex + 1) % items.length;
    updateCarousel();
}

function prevItem() {
    // Retrocede al elemento anterior, o va al último si está en el primero
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    updateCarousel();
}
