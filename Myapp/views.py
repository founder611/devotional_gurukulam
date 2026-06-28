from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def homepage(request):
    return render(request,'homepage.html')




# ==========================================
# SUBSCRIPTION EMAIL FUNCTION
# ==========================================
def emailenquiry(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        try:
            subscription_html = f"""
            <html>
            <body style="font-family: Arial; background:#f4f4f4; padding:30px;">
            <div style="max-width:600px; margin:auto; background:white; border-radius:15px; padding:30px;">
            <h1 style="color:#0b7d45; text-align:center;">🌿 Welcome to ECOMONKS</h1>
            <p>Thank you for subscribing to ECOMONKS.</p>
            <p>We are excited to have you as part of our growing family ❤️</p>
            </div>
            </body>
            </html>
            """
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("devotionalgurukulam@gmail.com", "lxtz bwip qpkw zewz")
            
            subscriber_msg = MIMEMultipart()
            subscriber_msg['From'] = "devotionalgurukulam@gmail.com"
            subscriber_msg['To'] = email
            subscriber_msg['Subject'] = "ECOMONKS Subscription"
            subscriber_msg.attach(MIMEText(subscription_html, 'html', 'utf-8'))
            server.sendmail("devotionalgurukulam@gmail.com", email, subscriber_msg.as_string())
            
            server.quit()
            
            return HttpResponse("""
            <script>
            alert('Subscribed Successfully');
            window.location='/';
            </script>
            """)
            
        except Exception as e:
            return HttpResponse(f"ERROR: {str(e)}")
    
    return HttpResponse("Invalid Request")

