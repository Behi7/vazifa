function showModal(message) {
    // Создаем элементы модального окна
    const modal = document.createElement('div');
    modal.classList.add('modal');
    const modalContent = document.createElement('div');
    modalContent.classList.add('modal-content');
    modalContent.textContent = message;
    const closeButton = document.createElement('button');
    closeButton.textContent = 'ОК';
    closeButton.classList.add('close-button');
    closeButton.addEventListener('click', () => {
      modal.remove();
    });
    modalContent.appendChild(closeButton);
    modal.appendChild(modalContent);
  
    // Добавляем модальное окно в DOM
    document.body.appendChild(modal);
  }
  