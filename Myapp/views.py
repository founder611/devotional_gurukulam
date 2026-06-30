from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def homepage(request):
    return render(request,'homepage.html')




def emailenquiry(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        message = request.POST.get("message")

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(
                "devotionalgurukulam@gmail.com",
                "lxtzbwipqpkwzewz"
            )

            # ===================================
            # EMAIL TO ADMIN
            # ===================================
            admin_html = f"""
            <html>
            <body style="font-family:Arial;background:#f7f7f7;padding:25px;">
            <div style="max-width:650px;margin:auto;background:#fff;padding:30px;border-radius:10px;">
                <h2 style="color:#8B4513;">🙏 New Course Enquiry</h2>

                <table cellpadding="8" cellspacing="0" width="100%">
                    <tr>
                        <td><b>Name</b></td>
                        <td>{name}</td>
                    </tr>
                    <tr>
                        <td><b>Email</b></td>
                        <td>{email}</td>
                    </tr>
                    <tr>
                        <td><b>Phone</b></td>
                        <td>{phone}</td>
                    </tr>
                    <tr>
                        <td><b>Course</b></td>
                        <td>{course}</td>
                    </tr>
                    <tr>
                        <td><b>Message</b></td>
                        <td>{message}</td>
                    </tr>
                </table>

            </div>
            </body>
            </html>
            """

            admin_msg = MIMEMultipart()
            admin_msg["From"] = "devotionalgurukulam@gmail.com"
            admin_msg["To"] = "devotionalgurukulam@gmail.com"
            admin_msg["Subject"] = "New Devotional Gurukulam Enquiry"
            admin_msg.attach(MIMEText(admin_html, "html"))

            server.sendmail(
                "devotionalgurukulam@gmail.com",
                "devotionalgurukulam@gmail.com",
                admin_msg.as_string(),
            )

            # ===================================
            # THANK YOU EMAIL TO USER
            # ===================================

            user_html = f"""
            <html>
            <body style="font-family:Arial;background:#f7f7f7;padding:25px;">
            <div style="max-width:650px;margin:auto;background:#ffffff;padding:35px;border-radius:12px;">

                <h1 style="color:#8B4513;text-align:center;">
                🙏 Devotional Gurukulam
                </h1>

                <p>Dear <strong>{name}</strong>,</p>

                <p>
                Thank you for contacting <strong>Devotional Gurukulam</strong>.
                We have received your enquiry successfully.
                </p>

                <p>
                Our team will get back to you shortly regarding your interest in:
                </p>

                <p style="font-size:18px;color:#b76e00;">
                <strong>{course}</strong>
                </p>

                <hr>

                <p><strong>Your Details</strong></p>

                <ul>
                    <li>Name : {name}</li>
                    <li>Email : {email}</li>
                    <li>Phone : {phone}</li>
                </ul>

                <p>
                We look forward to welcoming you on this sacred journey of
                learning, devotion and spiritual transformation.
                </p>

                <br>

                <p>
                Warm Regards,<br>
                <strong>Devotional Gurukulam</strong>
                </p>

            </div>
            </body>
            </html>
            """

            user_msg = MIMEMultipart()
            user_msg["From"] = "devotionalgurukulam@gmail.com"
            user_msg["To"] = email
            user_msg["Subject"] = "Thank You for Contacting Devotional Gurukulam"
            user_msg.attach(MIMEText(user_html, "html"))

            server.sendmail(
                "devotionalgurukulam@gmail.com",
                email,
                user_msg.as_string(),
            )

            server.quit()

            return HttpResponse("""
            <script>
                alert("Thank you! Your enquiry has been submitted successfully.");
                window.location.href="/";
            </script>
            """)

        except Exception as e:
            return HttpResponse(f"Error : {e}")

    return HttpResponse("Invalid Request")