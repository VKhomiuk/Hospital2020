$('.slider').slick({
    autoplay: true,
    autoplaySpeed: 15000,
    arrows: true,
    lazyLoad: 'progressive',
    prevArrow: '<div class="slickArrow slickPrev"><i class="im im-angle-left-circle"></i></div>',
    nextArrow: '<div class="slickArrow slickNext"><i class="im im-angle-right-circle"></i></div>',
});
window.onload=()=>{
    document.querySelector('.slider').classList.remove('hide')
}