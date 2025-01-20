document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', function () {
    if (typeof $ !== 'undefined') {
        $('#preloader').fadeOut();
        $('body').removeClass('hidden');
    }
}) : function () {
    if (typeof $ !== 'undefined') {
        $('#preloader').fadeOut();
        $('body').removeClass('hidden');
    }
}();