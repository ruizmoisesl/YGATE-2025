// Aquí puedes agregar funcionalidad si necesitas
// Como cambiar las categorías al hacer clic en los botones de navegación
document.querySelectorAll('.categoria-nav').forEach(button => {
    button.addEventListener('click', () => {
        alert('Navegar entre categorías');
    });
});
function desplazarIzquierda() {
    const contenedor = document.getElementById('listaCategorias');
    const anchoCategoria = document.querySelector('.categoria').offsetWidth + 20; // Obtiene el ancho de una categoría + el margen
    contenedor.scrollBy({ left: -anchoCategoria, behavior: 'smooth' }); // Desplaza por el ancho de una categoría
  }

  function desplazarDerecha() {
    const contenedor = document.getElementById('listaCategorias');
    const anchoCategoria = document.querySelector('.categoria').offsetWidth + 20; // Obtiene el ancho de una categoría + el margen
    contenedor.scrollBy({ left: anchoCategoria, behavior: 'smooth' }); // Desplaza por el ancho de una categoría
  }
