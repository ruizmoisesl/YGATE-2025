window.onload = function () {
    if (typeof $ !== 'undefined') {
        $('#preloader').fadeOut();
        $('body').removeClass('hidden');
    } else {
      console.error('jQuery no está cargado.');
    }
  }