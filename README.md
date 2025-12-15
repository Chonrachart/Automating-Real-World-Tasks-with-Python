# Automating-Real-World-Tasks-with-Python
Automating Real-World Tasks with Python google course that part of Google IT Automation with Python Professional Certificate

1.do change_format_image.py to convert original image.tiff with size 192x192 and anti-clockwisej 90 degree to image.jpg with size 128x128

# Final project
problem statment You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:
1.Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.
2.Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:
1.Run a script on your web server to monitor system health.
2.Send an email with an alert if the server is ever unhealthy.

scrip explain

1.def function generate email with attachment and with out attachment use email.message module and def function send email use SMTP module (email.py)

2.open image from file path and change file format to 600x400 in jpeg then save to new file (changeimage.py)

3.def function generate report pdf use reportlab module (reports.py)

4.to upload picture that process by (changeImage.py) to URL use request module (supplier_image_upload.py)

5.update feedback from user in txt respectively with image name to URL (run.py)  

6.create fruits data and use generate report pdf in reports.py and send it to email use generate email with attachment pdf report use generate email with 

  attachment and send it use send email function (report_email.py)
  
7.create health check monitor that send the email if condition is met (health_check.py)
