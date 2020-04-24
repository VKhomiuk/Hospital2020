const menu = document.querySelector('.header-top__body');
const contactInfo = document.querySelector('.contact-info');
const menuBtn = document.querySelector('.menu__item_btn');
const menuItems = document.querySelectorAll('.menu__item');

menuBtn.addEventListener('click', () => {
    for (let item of menuItems) {
        item.classList.toggle('hide');
    }
    menuItems.classList.toggle('hide');
});


var map;

function initialize() {
    var mapOptions = {
        zoom: 18,
        center: {lat: 49.2354, lng: 28.414}
    };
    map = new google.maps.Map(document.querySelector('.map'),
        mapOptions);

    var marker = new google.maps.Marker({

        position: {lat: 49.235429, lng: 28.414315},
        map: map
    });
    var infowindow = new google.maps.InfoWindow({
        content: '<p>Marker Location:' + marker.getPosition() + '</p>'
    });

    google.maps.event.addListener(marker, 'click', function () {
        infowindow.open(map, marker);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);


addEventListener("scroll", () => {
    const scrolled = document.scrollingElement.scrollTop;
    const position = menu.offsetTop;
    scrolled >= position && (menu.classList.add('fixed') , contactInfo.classList.add('hidden'));
    scrolled <= 40 && (menu.classList.remove('fixed') , contactInfo.classList.remove('hidden'));
});


let phoneInput = document.querySelector('.phone')
phoneInput.addEventListener('keydown', function (event) {
    if (!(event.key == 'ArrowLeft' || event.key == 'ArrowRight' || event.key == 'Backspace' || event.key == 'Tab')) {
        event.preventDefault()
    }
    const mask = '+38 (111) 111-11-11'; // Задаем маску

    if (/[0-9\+\ \-\(\)]/.test(event.key)) {
        // Здесь начинаем сравнивать this.value и mask
        // к примеру опять же
        let currentString = this.value;
        let currentLength = currentString.length;
        if (/[0-9]/.test(event.key)) {
            if (mask[currentLength] == '1') {
                this.value = currentString + event.key;
            } else {
                for (var i = currentLength; i < mask.length; i++) {
                    if (mask[i] == '1') {
                        this.value = currentString + event.key;
                        break;
                    }
                    currentString += mask[i];
                }
            }
        }
    }
});


const submitForm = document.getElementById('submitForm');
const modalWindow = document.getElementById('modalWindow');
const modalContent = document.querySelector('.modal-content');
const form = document.getElementById('form');


submitForm.onclick = () => {

    console.log(form.elements[0].value.length >= 5);
    console.log(form.elements[1].value.length === 13);
    console.log(form.elements[2].value.search(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)>=0);
    modalWindow.classList.add('show');
    if(form.elements[0].value.length >= 5 && form.elements[1].value.length >= 13 &&form.elements[2].value.search(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)>=0){
        modalContent.classList.remove("error");
        Array.from(form.elements).map((input) => input.value = '');
    }else{
        modalContent.innerHTML = `<span>Неправильно введені дані!</span>` ;
        modalContent.classList.add("error");

    }

   if(Array.from(form.elements).every((input) => {
       console.log(input.checkValidity());
       return input.checkValidity();
   }))  {
       modalWindow.classList.add('show');
       Array.from(form.elements).map((input) => input.value = '');
   }else{
       modalWindow.classList.add('show');
       modalContent.classList.add("error");
       modalContent.innerText = "некоректне введення"
   }

};



window.onclick = (e) => {
    e.target === modalWindow && modalWindow.classList.remove('show');
}


;




