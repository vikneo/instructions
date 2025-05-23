from django.apps import AppConfig


class InstructionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "instruction"

    def ready(self) -> None:
        import instruction.signals
