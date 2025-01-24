const fechaActual = new Date();
const dia = fechaActual.getDate();
const mes = (fechaActual.getMonth() + 1).toString().padStart(2, '0');
const año = fechaActual.getFullYear();
const fecha = `${dia}/${mes}/${año}`;

const inputSearch = document.getElementById('search');
const divProducts = document.getElementById('products');

inputSearch.addEventListener('input', () => {
    if (inputSearch.value.length > 0) {
        divProducts.style.display = 'flex';
        divProducts.animate.add('fadeIn');
    } else {
        divProducts.style.display = 'none';
    }
});

inputSearch.addEventListener('input', () => {
    const products = divProducts.children;
    for (let i = 0; i < products.length; i++) {
        const product = products[i];
        const productName = product.textContent.toLowerCase();
        const searchValue = inputSearch.value.toLowerCase();
        if (productName.includes(searchValue)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    }
});

inputNombre.addEventListener('input', () => {
    let nombreCliente = document.getElementById('nombreCliente');
    let inputNombre = document.getElementById('inputNombre');
    nombreCliente.textContent = inputNombre.value;
});

inputNit.addEventListener('input', () => {
    let nit = document.getElementById('nit');
    let inputNit = document.getElementById('inputNit');
    nit.textContent = inputNit.value;
});

inputTelefono.addEventListener('input', () => {
    let inputTelefono = document.getElementById('inputTelefono');
    let telefono = document.getElementById('telefono');
    telefono.textContent = inputTelefono.value;
});

inputDireccion.addEventListener('input', () => {
    let direccion = document.getElementById('direccion');
    direccion.textContent = inputDireccion.value;
});

document.getElementById('fecha').textContent = fecha;

let sectionCantidad = document.querySelector('.cantidad');
let precioProductoSeleccionado = 0;
document.addEventListener('DOMContentLoaded', () => {
    const productsContainer = document.getElementById('products');
    let precioFinal;

    productsContainer.addEventListener('click', (e) => {
        if (e.target.closest('button.product-button')) {
            const productButton = e.target.closest('button.product-button');
            const productName = productButton.querySelector('.product-name').textContent;
            const productPrice = productButton.querySelector('.product-price').textContent;
            precioProductoSeleccionado = parseInt(productPrice)

            sectionCantidad.style.display = 'flex';
            divProducts.style.display = 'none';

            const nombreProductoSpan = document.createElement('span');
            nombreProductoSpan.textContent = productName;
            document.getElementById('nombreProducto').appendChild(nombreProductoSpan);

            const precioUnidadSpan = document.createElement('span');
            precioUnidadSpan.textContent = productPrice;
            document.getElementById('precioUnidad').appendChild(precioUnidadSpan);
        }
    });
});

let buttonCantidad = document.getElementById('button-cantidad')
let PagoTotal = 0;
buttonCantidad.addEventListener('click', () => {
    let inputCantidad = parseInt(document.getElementById('inputCantidad').value) || 0;
    precioFinal = precioProductoSeleccionado * inputCantidad;


    const ProductoscantidadSpan = document.createElement('span');
    ProductoscantidadSpan.textContent = inputCantidad;
    document.getElementById('Productoscantidad').appendChild(ProductoscantidadSpan);

    const precioTotalSpan = document.createElement('span');
    precioTotalSpan.classList.add('spanPrecioTotal');
    precioTotalSpan.textContent = precioFinal;
    document.getElementById('precioTotal').appendChild(precioTotalSpan);

    let precioProductos = document.querySelectorAll('.spanPrecioTotal')
    let suma = 0;
    PagoTotal = suma
    precioProductos.forEach((precio) => {
        suma += parseInt(precio.innerHTML);
    });

    const spanTotalPagar = document.createElement('span');
    spanTotalPagar.textContent = suma;
    document.querySelector('#totalPagar').innerHTML = `<span>${parseInt(suma)}</span>`;

    sectionCantidad.style.display = 'none';
});


const buttonTerminar = document.getElementById('button-terminar');

document.addEventListener('DOMContentLoaded', () => {
    const buttonTerminar = document.getElementById('button-terminar');

    buttonTerminar.addEventListener('click', () => {
        printSection('factura');
    });

    function printSection(sectionId) {
        const printContents = document.getElementById(sectionId).innerHTML;
        const originalContents = document.body.innerHTML;

        document.body.innerHTML = printContents;
        window.print();
        document.body.innerHTML = originalContents;
        window.location.reload(); // Recargar la página para restaurar el contenido original
    }
});