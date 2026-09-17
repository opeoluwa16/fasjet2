(function(){
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('mobileMenu');
  if(toggle && menu){
    toggle.addEventListener('click', () => {
      menu.classList.toggle('open');
    });
  }

  const form = document.getElementById('contact-form');
  if(form){
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('cf-name').value;
      const email = document.getElementById('cf-email').value;
      const message = document.getElementById('cf-message').value;
      const subject = encodeURIComponent('Website Enquiry from ' + name);
      const body = encodeURIComponent(message + '\n\nFrom: ' + name + ' (' + email + ')');
      const url = 'https://mail.google.com/mail/?view=cm&fs=1&to=fasjetsolutions@gmail.com&su=' + subject + '&body=' + body;
      window.open(url, '_blank');
    });
  }
})();