from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^personal_diary/home', 'personal_diary.views.home'),
     url(r'^personal_diary/tasks', 'personal_diary.views.tasks'),
     url(r'^personal_diary/do', 'personal_diary.views.do'),
    # url(r'^diary/', include('diary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
