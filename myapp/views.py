from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse('به اقبال خوش آمدید')

# در پایتون ۳.۶ به بعد، اگر قبل از رشته‌ای که داخلش {} دارد حرف 
# f
#  بگذارید، پایتون به‌صورت خودکار هر چیزی که داخل {} نوشته شده
#  را به عنوان نام متغیر شناسایی کرده
#  و مقدار آن را در رشته قرار می‌دهد.
# http://127.0.0.1:8000/sum-varible/5/6
def sumAB(request, a , b):
    res = a + b
    return HttpResponse(f'the sum is  equal to {res}')

# فشار محاسباتی روی سرور میاد
def print_text_n_times(request,text,n):
    inner_text=''
    for i in range(n):
        inner_text +=f'<li>{text}</li>'
    
    outer_text =f'<ul>{inner_text}</ul>'

    return HttpResponse(outer_text)
#میخوایم عدد اعشاری در هم ضرب کنیم
# فلوت رو متوجه نمیشه برای همین اون سمت استرینگ میفرستیم اینجا تبدیل میکنیم به فلوت path  متد 
#http://127.0.0.1:8000/product/5.5/6/10
def product(request,a,b,c):
    fa=float(a)
    fb=float(b)
    fc=float(c)
    result=fa*fb*fc
    return HttpResponse(result)

# http://127.0.0.1:8000/buy/6000/5500
def buy(request,price,mymoney):
    price=float(price)
    mymoney=float(mymoney)

    if(price <= mymoney):
        return HttpResponse('میتونی بخریش سلطان')
    else:
        return HttpResponse('شرمنده پول نداری داداش')



# تفاوت render() و HttpResponse()
# HttpResponse(): رشته HTML را مستقیماً برمی‌گرداند (با f-string)
# render(): فایل HTML را لود می‌کند و متغیرها را به آن می‌فرستد


# http://127.0.0.1:8000/units/
def get_unit(request):
    # لیست دروس و واحدها (می‌توانید تغییر دهید)
    courses = [
        {'name': 'برنامه نویسی وب', 'units': 3},
        {'name': 'پایگاه داده', 'units': 3},
        {'name': 'سیستم عامل', 'units': 3},
        {'name': 'زبان تخصصی', 'units': 2},
        {'name': 'آزمایشگاه شبکه', 'units': 1},
        {'name': 'ریاضی مهندسی', 'units': 3},
    ]
    
    # محاسبه مجموع کل واحدها
    total_units = sum(course['units'] for course in courses)
    
    # ساخت ردیف‌های جدول با حلقه
    rows = ''
    for i, course in enumerate(courses, 1):
        rows += f'''
        <tr>
            <td>{i}</td>
            <td>{course['name']}</td>
            <td>{course['units']}</td>
        </tr>
        '''
    
    # HTML کامل با استایل
    html = f'''
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>واحدهای دانشگاهی</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Tahoma', 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 40px 20px;
                direction: rtl;
            }}
            
            .container {{
                max-width: 800px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                overflow: hidden;
            }}
            
            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                text-align: center;
            }}
            
            .header h1 {{
                font-size: 28px;
                margin-bottom: 10px;
            }}
            
            .header p {{
                font-size: 16px;
                opacity: 0.9;
            }}
            
            .content {{
                padding: 30px;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            
            thead {{
                background: #667eea;
                color: white;
            }}
            
            th, td {{
                padding: 15px;
                text-align: right;
                border-bottom: 1px solid #e0e0e0;
            }}
            
            th {{
                font-weight: bold;
                font-size: 16px;
            }}
            
            tbody tr:hover {{
                background: #f5f5f5;
                transition: background 0.3s;
            }}
            
            .total-row {{
                background: #f0f0f0;
                font-weight: bold;
                font-size: 18px;
            }}
            
            .total-row td {{
                border-top: 3px solid #667eea;
                padding: 20px 15px;
            }}
            
            .summary {{
                display: flex;
                justify-content: space-around;
                margin-top: 30px;
                padding: 20px;
                background: #f9f9f9;
                border-radius: 10px;
            }}
            
            .summary-item {{
                text-align: center;
            }}
            
            .summary-item .number {{
                font-size: 36px;
                font-weight: bold;
                color: #667eea;
                display: block;
            }}
            
            .summary-item .label {{
                font-size: 14px;
                color: #666;
                margin-top: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📚 واحدهای دانشگاهی</h1>
                <p>لیست دروس اخذ شده در ترم جاری</p>
            </div>
            
            <div class="content">
                <table>
                    <thead>
                        <tr>
                            <th>ردیف</th>
                            <th>نام درس</th>
                            <th>تعداد واحد</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                        <tr class="total-row">
                            <td colspan="2">مجموع کل واحدها</td>
                            <td>{total_units} واحد</td>
                        </tr>
                    </tbody>
                </table>
                
                <div class="summary">
                    <div class="summary-item">
                        <span class="number">{len(courses)}</span>
                        <span class="label">تعداد دروس</span>
                    </div>
                    <div class="summary-item">
                        <span class="number">{total_units}</span>
                        <span class="label">مجموع واحدها</span>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    
    return HttpResponse(html)

    
# http://127.0.0.1:8000/unitsmodular/
def get_unit_modular(request):
     # لیست دروس و واحدها (می‌توانید تغییر دهید)
    courses = [
        {'name': 'برنامه نویسی وب', 'units': 3},
        {'name': 'پایگاه داده', 'units': 3},
        {'name': 'سیستم عامل', 'units': 3},
        {'name': 'زبان تخصصی', 'units': 2},
        {'name': 'آزمایشگاه شبکه', 'units': 1},
        {'name': 'ریاضی مهندسی', 'units': 3},
    ]
    
    # محاسبه مجموع کل واحدها
    total_units = sum(course['units'] for course in courses)
    
    # ساخت ردیف‌های جدول با حلقه
    rows = ''
    for i, course in enumerate(courses, 1):
        rows += f'''
        <tr>
            <td>{i}</td>
            <td>{course['name']}</td>
            <td>{course['units']}</td>
        </tr>
        '''
    
    # ✅ ارسال متغیرها به template
    context = {
        'courses': courses,
        'total_units': total_units,
        'rows': rows,
        'courses_count': len(courses),  # تعداد دروس
    }
    
    return render(request, 'myapp/unit-page.html', context)




# http://127.0.0.1:8000/hello/matin
def hello_user(request, username):
    context = {
        'username': username,
    }
    return render(request, 'myapp/hello-user.html', context)







import json

    # داده‌های JSON (اصلاح شده)

# member_data = '''
#     {
#       "members": [
#         {
#           "member_info": {
#             "name": "زهرا سعادتی",
#             "member_id": "1",
#             "major": "علوم کامپیوتر",
#             "total_borrows": 3
#           },
#           "books": [
#             {
#               "id": 1,
#               "title": "برنامه‌نویسی پایتون",
#               "author": "ناصر کریمی",
#               "borrow_date": "1405/02/10",
#               "status": "برگشت داده نشده"
#             },
#             {
#               "id": 2,
#               "title": "تحلیل داده‌ها",
#               "author": "مهدی سلطانی",
#               "borrow_date": "1405/02/02",
#               "status": "برگشت داده شده"
#             },
#             {
#               "id": 3,
#               "title": "هوش مصنوعی مقدماتی",
#               "author": "لیلا شریفی",
#               "borrow_date": "1405/01/28",
#               "status": "برگشت داده نشده"
#             }
#           ]
#         },
#         {
#           "member_info": {
#             "name": "امیر حسینی",
#             "member_id": "2",
#             "major": "مهندسی برق",
#             "total_borrows": 2
#           },
#           "books": [
#             {
#               "id": 1,
#               "title": "مدارهای الکتریکی",
#               "author": "عباس جوادی",
#               "borrow_date": "1405/02/05",
#               "status": "برگشت داده شده"
#             },
#             {
#               "id": 2,
#               "title": "سیگنال‌ها و سیستم‌ها",
#               "author": "علی علیزاده",
#               "borrow_date": "1405/02/08",
#               "status": "برگشت داده نشده"
#             }
#           ]
#         }
#       ]
#     }
#     '''
#     # تبدیل JSON به دیکشنری پایتون
# data = json.loads(member_data)

import os

from django.conf import settings
# ✅ لود کردن داده‌ها فقط یک بار
DATA_FILE = os.path.join(settings.BASE_DIR, 'data', 'members.json')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# http://127.0.0.1:8000/library/1
def library_member(request, member_id):

    

    
    # پیدا کردن عضو مورد نظر
    member = None
    for m in data['members']:
        if m['member_info']['member_id'] == member_id:
            member = m
            break
    
    # اگر عضو پیدا نشد
    if not member:
        return HttpResponse(f'<h1 style="text-align:center; font-family:Tahoma; margin-top:50px;">❌ عضو با شناسه {member_id} یافت نشد</h1>')
    
    # محاسبه تعداد کتاب‌های برگردانده نشده
    unreturned_books = [book for book in member['books'] if book['status'] == 'برگشت داده نشده']
    unreturned_count = len(unreturned_books)
    
    # # ساخت ردیف‌های جدول
    # books_rows = ''
    # for book in member['books']:
    #     # تعیین کلاس CSS بر اساس وضعیت
    #     status_class = 'returned' if book['status'] == 'برگشت داده شده' else 'unreturned'
        
    #     books_rows += f'''
    #     <tr>
    #         <td>{book['id']}</td>
    #         <td>{book['title']}</td>
    #         <td>{book['author']}</td>
    #         <td>{book['borrow_date']}</td>
    #         <td class="{status_class}">{book['status']}</td>
    #     </tr>
    #     '''
    
    # # ساخت لیست کتاب‌های برگردانده نشده
    # unreturned_list = ''
    # if unreturned_books:
    #     for book in unreturned_books:
    #         unreturned_list += f'<li><strong>{book["title"]}</strong> - نویسنده: {book["author"]}</li>'
    # else:
    #     unreturned_list = '<li style="color:green;">✅ همه کتاب‌ها برگردانده شده‌اند</li>'
    
    # # ارسال متغیرها به template
    # context = {
    #     'member_name': member['member_info']['name'],
    #     'member_id': member['member_info']['member_id'],
    #     'major': member['member_info']['major'],
    #     'total_borrows': member['member_info']['total_borrows'],
    #     'books_rows': books_rows,
    #     'unreturned_count': unreturned_count,
    #     'unreturned_list': unreturned_list,
    #     'has_unreturned': unreturned_count > 0,
    # }


    # ✅ محاسبه همه آمار در View
    books = member['books']
    unreturned_books = [book for book in books if book['status'] == 'برگشت داده نشده']
    returned_books = [book for book in books if book['status'] == 'برگشت داده شده']
    
    # ✅ محاسبه تعداد
    total_borrows = len(books)
    unreturned_count = len(unreturned_books)
    returned_count = len(returned_books)
    # ✅به template ارسال همه متغیرها
    context = {
        'member_name': member['member_info']['name'],
        'member_id': member['member_info']['member_id'],
        'major': member['member_info']['major'],
        'total_borrows': total_borrows,
        'returned_count': returned_count,  
        'unreturned_count': unreturned_count,  
        'books': books,
        'unreturned_books': unreturned_books,
    }
    
    return render(request, 'myapp/library-member.html', context)
