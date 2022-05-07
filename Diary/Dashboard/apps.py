from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'Dashboard'
  # add this function
    def ready(self):
        import Dashboard.signals
