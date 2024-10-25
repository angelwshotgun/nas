from flask import Flask, render_template, request, make_response
import pdfkit
app = Flask(__name__)

# Cấu hình wkhtmltopdf (bỏ qua nếu không dùng ở preview)
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Đường dẫn chính xác
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

@app.route('/')
def index():
    return render_template('form.html')  # Trang để nhập thông tin

@app.route('/create_pdf', methods=['POST'])
def create_pdf():
    # Nhận dữ liệu từ form HTML
    name = request.form.get('name')
    guests = request.form.get('guests')
    stay_dates = request.form.get('stay_dates')
    room_info = request.form.get('room_info')
    grand_total = request.form.get('grand_total')
    total_payment = request.form.get('total_payment')
    services_included = request.form.get('services_included')
    other_services = request.form.get('other_services')
    payment_note = request.form.get('payment_note')
    payment_info = request.form.get('payment_info')

    # Render template với dữ liệu
    rendered_html = render_template(
        'pdf_template.html',
        name=name,
        guests=guests,
        stay_dates=stay_dates,
        room_info=room_info,
        grand_total=grand_total,
        total_payment=total_payment,
        services_included=services_included,
        other_services=other_services,
        payment_note=payment_note,
        payment_info=payment_info
    )

    # Chuyển đổi HTML sang PDF
    pdf = pdfkit.from_string(rendered_html, False, configuration=config)

    # Trả về file PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=confirmation.pdf'

    return response
    # Nhận dữ liệu từ form HTML
    name = request.form.get('name')
    guests = request.form.get('guests')
    stay_dates = request.form.get('stay_dates')
    room_type = request.form.get('room_type')
    room_price = request.form.get('room_price')
    total_payment = request.form.get('total_payment')
    services_included = request.form.get('services_included')
    other_services = request.form.get('other_services')
    payment_note = request.form.get('payment_note')
    payment_info = request.form.get('payment_info')

    # Render HTML mà không tạo file PDF
    return render_template(
        'pdf_template.html',
        name=name,
        guests=guests,
        stay_dates=stay_dates,
        room_type=room_type,
        room_price=room_price,
        total_payment=total_payment,
        services_included=services_included,
        other_services=other_services,
        payment_note=payment_note,
        payment_info=payment_info
    )

if __name__ == '__main__':
    app.run(debug=True)
