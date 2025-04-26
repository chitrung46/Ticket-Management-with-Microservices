const API_URL = 'http://127.0.0.1:8000';

async function loadBuses() {
  try {
    // Gửi yêu cầu fetch tới API để lấy dữ liệu
    const res = await fetch(API_URL + '/buses/');  // Cập nhật API_URL nếu cần
    if (!res.ok) {
      throw new Error('Lỗi khi tải dữ liệu từ API');
    }
    
    const buses = await res.json();  // Chuyển đổi phản hồi thành JSON
    const tbody = document.getElementById('bus-table-body');  // Lấy tbody của bảng
    tbody.innerHTML = '';  // Xóa dữ liệu cũ trong bảng

    // Tạo HTML cho các hàng trong bảng
    let rows = '';
    buses.forEach((bus, index) => {
      const row = `
        <tr>
          <td>${index + 1}</td>
          <td>${bus.num_plate}</td>
          <td>${bus.brand}</td>
          <td>${bus.color}</td>
          <td>${bus.bus_type_id}</td>
          <td>
            <button class="btn btn-sm btn-warning" onclick='editBus(${JSON.stringify(bus)})'>Sửa</button>
            <button class="btn btn-sm btn-danger" onclick='deleteBus("${bus.id}")'>Xoá</button>
          </td>
        </tr>
      `;
      rows += row;  // Gộp tất cả các hàng vào một chuỗi
    });

    // Chèn tất cả các hàng vào bảng chỉ một lần
    tbody.innerHTML = rows;

  } catch (error) {
    console.error('Error:', error);
    // Xử lý lỗi (thí dụ: hiển thị thông báo lỗi trên giao diện)
    alert('Có lỗi xảy ra khi tải danh sách xe buýt');
  }
}


// function editBus(bus) {
//   document.getElementById('bus-id').value = bus.id;
//   document.getElementById('num_plate').value = bus.num_plate;
//   document.getElementById('brand').value = bus.brand;
//   document.getElementById('color').value = bus.color;
//   document.getElementById('bus_type_id').value = bus.bus_type_id;
//   new bootstrap.Modal(document.getElementById('busModal')).show();
// }

// async function deleteBus(id) {
//   if (confirm('Bạn có chắc chắn muốn xoá xe này?')) {
//     await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
//     loadBuses();
//   }
// }

// document.getElementById('bus-form').addEventListener('submit', async (e) => {
//   e.preventDefault();
//   const id = document.getElementById('bus-id').value;
//   const data = {
//     num_plate: document.getElementById('num_plate').value,
//     brand: document.getElementById('brand').value,
//     color: document.getElementById('color').value,
//     bus_type_id: document.getElementById('bus_type_id').value,
//   };
//   const method = id ? 'PUT' : 'POST';
//   const url = id ? `${API_URL}/${id}` : API_URL;

//   await fetch(url, {
//     method,
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify(data)
//   });

//   bootstrap.Modal.getInstance(document.getElementById('busModal')).hide();
//   e.target.reset();
//   loadBuses();
// });

window.onload = loadBuses;
