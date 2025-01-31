const { default: Swal } = require("sweetalert2");

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
        let inputTelefono = document.getElementById('inputTelefono').value;    
        let inputNit = document.getElementById('inputNit').value;
        let inputNombre = document.getElementById('inputNombre').value;
        let inputDireccion = document.getElementById('inputDireccion').value

        if (inputNombre === '' || inputNit === '' || inputDireccion === ''|| inputTelefono == '' ){
            alert('Termina de rellenar los campos faltantes')
        }else{
            addExtraElementsToFactura();
            printSection('factura');
            setTimeout(() => {
                window.location.reload();
            }, 1000);
        }
    });

    function addExtraElementsToFactura() {
        const factura = document.getElementById('factura');
        
        // Crear un nuevo elemento para agregar a la factura
        const extraElement = document.createElement('div');
        extraElement.classList.add('extradiv')
        extraElement.innerHTML = `
            <img src="/static/img/icons/icono.png" alt="logo" width="100px" heigth="100px">
            <p style="font-weight:bold;">Gracias por tu compra!</p>
        `;
        
        factura.appendChild(extraElement);
    }

    function printSection(sectionId) {
        printJS({
            printable: sectionId,
            type: 'html',
            targetStyles: ['*'],
            css: '/static/css/sales.css', 
            style: `
                @page { 
                    size: auto;  /* auto es el valor inicial */
                    margin: 20mm; 
                }
                #factura {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                    padding: 0;
                }
            `,
            scanStyles: false 
        });
    }
});