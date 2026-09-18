(function(){
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('mobileMenu');
  if(toggle && menu){ toggle.addEventListener('click', function(){ menu.classList.toggle('open'); }); }

  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      }
    });
  }, {threshold:0.2});

  document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });

  document.querySelectorAll('.stagger').forEach(function(group){
    var items = group.querySelectorAll('.glass-card, .proj-card');
    items.forEach(function(item, i){
      item.style.transitionDelay = (i * 0.09) + 's';
      io.observe(item);
    });
  });

  var form = document.getElementById('contact-form');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var name = document.getElementById('cf-name').value;
      var company = document.getElementById('cf-company').value;
      var phone = document.getElementById('cf-phone').value;
      var message = document.getElementById('cf-message').value;
      var subject = encodeURIComponent('Website Enquiry from ' + name);
      var body = encodeURIComponent(message + '\n\nFrom: ' + name + (company ? ' (' + company + ')' : '') + '\nPhone: ' + phone);
      var url = 'https://mail.google.com/mail/?view=cm&fs=1&to=fasjetsolutions@gmail.com&su=' + subject + '&body=' + body;
      window.open(url, '_blank');
    });
  }
})();