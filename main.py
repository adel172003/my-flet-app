import flet as ft
from flet import *

def main(page: ft.Page):
    # إعداد الصفحة
    page.title = "تطبيقي مع إعلانات"
    page.window.width = 400
    page.window.height = 800
    page.padding = 20
    
    # معرفات الإعلانات الاختبارية
    REWARDED_AD_UNIT_ID = "ca-app-pub-3940256099942544/5224354917"
    BANNER_AD_UNIT_ID = "ca-app-pub-3940256099942544/6300978111"
    
    # متغير لتتبع نقاط المستخدم
    user_points = 0
    
    # نص لعرض النقاط
    points_text = Text(f"نقاطك: {user_points}", size=20, weight="bold")
    
    # إنشاء مساحة إعلان البانر
    banner_ad = Container(
        content=Text("مساحة إعلان البانر", size=14, color="white", text_align="center"),
        width=320,
        height=50,
        bgcolor=colors.BLUE_GREY_400,
        border_radius=5,
        alignment=alignment.center,
    )
    
    # دالة لعرض إعلان المكافآت وزيادة النقاط
    def show_rewarded_ad(e):
        nonlocal user_points
        user_points += 10
        points_text.value = f"نقاطك: {user_points}"
        
        page.open = SnackBar(
            content=Text("مبروك! حصلت على 10 نقاط"),
            action="حسناً"
        )
        page.update()
    
    # زر لعرض إعلان المكافآت
    watch_ad_button = ElevatedButton(
        content=Row(
            controls=[
                Icon(icons.PLAY_CIRCLE),
                Text("شاهد إعلان للحصول على 10 نقاط", size=16)
            ],
            alignment=MainAxisAlignment.CENTER
        ),
        style=ButtonStyle(
            color={
                ControlState.DEFAULT: colors.WHITE,
                ControlState.HOVERED: colors.WHITE
            },
            bgcolor={
                ControlState.DEFAULT: colors.BLUE,
                ControlState.HOVERED: colors.BLUE_700
            }
        ),
        on_click=show_rewarded_ad
    )
    
    # محتوى التطبيق الرئيسي
    main_content = Column(
        controls=[
            Text("لعبتي الرائعة!", size=30, weight="bold"),
            Container(height=20),
            points_text,
            Container(height=20),
            watch_ad_button,
            Container(height=20),
            Text("شاهد الإعلانات لكسب المزيد من النقاط!", size=16),
        ],
        spacing=10,
        alignment=MainAxisAlignment.START,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )
    
    # تنظيم المحتوى مع إعلان البانر في الأسفل
    page_content = Column(
        controls=[
            main_content,
            Container(  # مسافة مرنة
                expand=True
            ),
            banner_ad,  # إعلان البانر في الأسفل
        ],
        spacing=10,
        expand=True
    )
    
    page.add(page_content)
    page.update()

if __name__ == "__main__":
    ft.app(target=main) 
