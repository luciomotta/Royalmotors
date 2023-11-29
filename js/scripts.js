document.getElementById('quoteButton').addEventListener('click', function() {
    document.getElementById('quoteModal').style.display = 'block';
});

document.getElementsByClassName('close')[0].addEventListener('click', function() {
    document.getElementById('quoteModal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('quoteModal')) {
        document.getElementById('quoteModal').style.display = 'none';
    }
});



//lOGICA DO FORMULARIO
function validateForm() {
    const cpf = document.getElementById('cpf').value;
    const phone = document.getElementById('phone').value;
    const hasCar = document.querySelector('input[name="hasCar"]:checked');
  
    // RegEx for CPF validation
    const cpfRegex = /^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$/;
  
    if (!cpfRegex.test(cpf)) {
      alert('Por favor, insira um CPF válido.');
      return false;
    }
  
    // Additional validation for phone number and car selection if needed
  
    return true; // Form submission allowed
  }
  
  // Formatação do CPF
const cpfInput = document.getElementById('cpf');
cpfInput.addEventListener('input', (e) => {
    let value = e.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
    if (value.length > 3) {
        value = value.replace(/^(\d{3})/, '$1.');
    }
    if (value.length > 7) {
        value = value.replace(/^(\d{3})\.(\d{3})/, '$1.$2.');
    }
    if (value.length > 11) {
        value = value.replace(/^(\d{3})\.(\d{3})\.(\d{3})/, '$1.$2.$3-');
    }
    e.target.value = value;
});

// Formatação do telefone
const phoneInput = document.getElementById('phone');
phoneInput.addEventListener('input', (e) => {
    let value = e.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
    if (value.length > 2 && value.length < 7) {
        value = value.replace(/^(\d{2})(\d{1,4})/, '($1) $2');
    } else if (value.length >= 7 && value.length < 11) {
        value = value.replace(/^(\d{2})(\d{1,4})(\d{1,4})/, '($1) $2-$3');
    } else {
        value = value.replace(/^(\d{2})(\d{1,5})(\d{1,4})/, '($1) $2-$3');
    }
    e.target.value = value;
});
