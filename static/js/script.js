document.addEventListener('DOMContentLoaded', () => {
 const synth = window.speechSynthesis;

 document.querySelectorAll('.listen-btn').forEach(btn => {
  btn.addEventListener('click', () => {
   synth.cancel();
   const utterance = new SpeechSynthesisUtterance(btn.getAttribute('data-speak'));
   utterance.rate = 1.0;
   utterance.pitch = 0.9;
   synth.speak(utterance);
  });
 });

 const typeText = (element) => {
  const text = element.getAttribute('data-fulltext');
  let i = 0;
  const interval = setInterval(() => {
   element.textContent += text[i];
   i++;
   if (i === text.length) clearInterval(interval);
  }, 35);
 };

 const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
   if (entry.isIntersecting) {
    entry.target.style.opacity = '1';
    entry.target.style.transform = 'translateY(0)';

    const summary = entry.target.querySelector('.ai-summary');
    if (summary && !summary.classList.contains('active')) {
     typeText(summary);
     summary.classList.add('active');
    }
   }
  });
 }, { threshold: 0.1 });

 document.querySelectorAll('.glass-card').forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(40px)';
  observer.observe(card);
 });
});