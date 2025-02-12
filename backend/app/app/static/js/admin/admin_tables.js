// Поиск по таблице
document.querySelector('.search').addEventListener('input', function(e) {
    const searchText = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('.table tbody tr');
    
    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(searchText) ? '' : 'none';
    });
  });
  
  // Сортировка по столбцам
  document.querySelectorAll('.table th').forEach(header => {
    header.addEventListener('click', function() {
      const index = Array.from(this.parentNode.children).indexOf(this);
      const rows = Array.from(document.querySelectorAll('.table tbody tr'));
      const isNumeric = index === 1 || index === 2;
      
      rows.sort((a, b) => {
        const aVal = a.children[index].textContent;
        const bVal = b.children[index].textContent;
        
        if (isNumeric) {
          return parseInt(aVal.replace(/[^0-9]/g, '')) - parseInt(bVal.replace(/[^0-9]/g, ''));
        }
        return aVal.localeCompare(bVal);
      });
      
      const tbody = document.querySelector('.table tbody');
      rows.forEach(row => tbody.appendChild(row));
    });
  });
  
  // Обработка кнопок удаления
  document.querySelectorAll('.btn-danger').forEach(btn => {
    btn.addEventListener('click', function() {
      if (confirm('Вы уверены, что хотите удалить эту таблицу?')) {
        const row = this.closest('tr');
        row.style.opacity = '0';
        setTimeout(() => row.remove(), 300);
      }
    });
  });
  
  // Обработка кнопок просмотра
  document.querySelectorAll('.btn-success').forEach(btn => {
    btn.addEventListener('click', function() {
      const tableName = this.closest('tr').querySelector('td').textContent;
      alert(`Просмотр таблицы: ${tableName}`);
    });
  });
  
  // Пагинация
  document.querySelectorAll('.page-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelector('.page-btn.active').classList.remove('active');
      this.classList.add('active');
    });
  });