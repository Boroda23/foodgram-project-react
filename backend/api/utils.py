import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def generate_shopping_cart_report(shopping_cart):
    buffer = io.BytesIO()
    page = canvas.Canvas(buffer)
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    x_position, y_position = 50, 800

    page.setFont('Vera', 14)
    if shopping_cart:
        indent = 20
        page.drawString(x_position, y_position, 'Cписок покупок:')
        for index, recipe in enumerate(shopping_cart, start=1):
            page.drawString(
                x_position, y_position - indent,
                f'{index}. {recipe["ingredients__name"]} - '
                f'{recipe["amount"]} '
                f'{recipe["ingredients__measurement_unit"]}.')
            y_position -= 15
            if y_position <= 50:
                page.showPage()
                y_position = 800
        page.save()
        buffer.seek(0)
        return buffer
    page.setFont('Vera', 24)
    page.drawString(
        x_position,
        y_position,
        'Cписок покупок пуст!')
    page.save()
    buffer.seek(0)
    return buffer
