window.addEventListener('load', function() {
    let selectCards = document.querySelectorAll('.info-select__card')
    let content = document.querySelectorAll('.info')
    let headerBtns = document.querySelectorAll('.header__navigation-btn')
    let docsBlocks = document.querySelectorAll('.main-docs-blocks-block')
    let docsBtns = document.querySelectorAll('.main-docs-btns__btn')
    let accordeons = document.querySelectorAll('.accordeon')
  
    selectCards.forEach(item => item.addEventListener('click', e => {
        let selectCardsTarget = e.target.getAttribute('data-card');
        selectCards.forEach(el => el.classList.remove('is-active'));
        content.forEach(el => el.classList.remove('is-active'));
        item.classList.add('is-active');
        document.getElementById(selectCardsTarget).classList.add('is-active');
    }));

    headerBtns.forEach(item => item.addEventListener('click', e => {

        // Prevent default behaviour - reload
        e.preventDefault()

        let targetClass = 'main-' + e.target.getAttribute('for')

        let arr = Array.from(document.querySelector("main").children)

        arr.forEach(item => {
            item.classList.remove('is-active')

            if (item.classList.contains(targetClass)) {
                item.classList.add('is-active')
            }
        })

        headerBtns.forEach(item => item.classList.remove('is-active'))
        e.target.classList.add('is-active')
    }))

    docsBtns.forEach(item => item.addEventListener('click', e => {
        let targetClass = e.target.getAttribute("for")

        let blocks = Array.from(docsBlocks)
        console.log(blocks.forEach(el => {
            el.classList.add("hidden")
           
            if (el.classList.contains(targetClass)) {
                el.classList.remove("hidden")
            }
        }));

        docsBtns.forEach(item => item.classList.remove('is-active'))
        e.target.classList.add('is-active')
    }))

    document.querySelectorAll('.info-rules__title').forEach((el) => {
        el.addEventListener('click', () => {
            const parent = el.parentNode;
            if (parent.classList.contains('info-rules__main_active')) {
                parent.classList.remove('info-rules__main_active');
            } else {
                document.querySelectorAll('.info-rules__main').forEach((child) => child.classList.remove('info-rules__main_active'))
                parent.classList.add('info-rules__main_active');
            }
            // parent.classList.toggle('information-rules__main_active');
        })
    });

    accordeons.forEach(item => {
        let icons = item.querySelectorAll(".accordeon-header__icon")
        
        icons.forEach(el => {
            el.addEventListener("click", e => {
                if (e.target.classList.contains("accordeon-header__icon_close")) {
                    item.querySelector(".accordeon-block").classList.add("hidden")
                }
                else {
                    item.querySelector(".accordeon-block").classList.remove("hidden")
                }

                icons.forEach(el => {el.classList.remove("hidden")})
                e.target.classList.add("hidden")
            });
        }) 
    })


});

// Navbar header
let nav_button = document.getElementById("nav-btn");
let navbar = document.getElementsByClassName("header__navbar")[0];

nav_button.addEventListener("click", e => {
    if (!navbar.classList.contains("header__navbar--open")) {
        navbar.classList.add("header__navbar--open");
    }
    else {
        navbar.classList.remove("header__navbar--open");
    }
});

let dorm_btn = document.getElementById("dormlist-btn");
let dorm_list = document.getElementsByClassName("header__navbar-links__dorms-list")[0];

dorm_btn.addEventListener("click", e => {
    if (!dorm_list.classList.contains("header__navbar-links__dorms-list--open")) {
        dorm_list.classList.add("header__navbar-links__dorms-list--open");
        dorm_btn.classList.add("dormlist-btn--active");
    }
    else {
        dorm_list.classList.remove("header__navbar-links__dorms-list--open");
        dorm_btn.classList.remove("dormlist-btn--active");
    }
});

//Links
let links = document.getElementsByClassName("link");

function linkOpen(n) {
    links[n-1].classList.toggle("link--active")
}

//Dorms Pagination
let dormPaginationButton = document.getElementsByClassName("dorm-pagination__button");

function dormPick(n) {
    let dormPaginationButtonActive = document.getElementsByClassName("dorm-pagination__button-active")[0];
    dormPaginationButtonActive.classList.remove("dorm-pagination__button-active");
    dormPaginationButton[n-1].classList.add("dorm-pagination__button-active");
}