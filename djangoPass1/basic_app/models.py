from django.db import models
from django.contrib.auth.models import User
from threading import Thread
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):

        return "{self.user.username}"

    
    threads = []
    for i in range(1):
        threads.append(Thread(target=upload))
        threads[-1].start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


