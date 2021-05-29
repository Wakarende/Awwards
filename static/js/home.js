// const mainNavigation = document.querySelector(".main-navigation");
// const overlay = mainNavigation.querySelector(".overlay");
// const toggler = mainNavigation.querySelector(".navbar-toggler");

// const openSideNav = () => mainNavigation.classList.add("active");
// const closeSideNav = () => mainNavigation.classList.remove("active");

// document.addEventListener("swiped-right", openSideNav);
// document.addEventListener("swiped-left", closeSideNav);
// toggler.addEventListener("click", openSideNav);
// overlay.addEventListener("click", closeSideNav);

// $(document).ready(function() {
//   $(".button-collapse").sideNav({
//     breakpoint: 1200
//   });
//     // SideNav Scrollbar Initialization
//     var sideNavScrollbar = document.querySelector('.custom-scrollbar');
//     var ps = new PerfectScrollbar(sideNavScrollbar);
// });

$(function () {
  $("#mdb-lightbox-ui").load("{% static 'mdb-addons/mdb-lightbox-ui.html' %}");
});