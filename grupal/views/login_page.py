import reflex as rx
from ..modelos.estudiantes import *
from ..servicios.user_servicio import *

class PageState(rx.State):
    pass

@rx.page(route="/login")
def login_page() -> rx.Component:
    return rx.container(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Iniciar Sesión", value="login"),
                rx.tabs.trigger("Registrarse", value="signup"),
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("Nombre de usuario", "Ingrese su usuario", "text", "username"),
                        form_fields("Contraseña", "Ingrese su contraseña", "password", "password"),
                        rx.button("Iniciar Sesión", type="submit", color_scheme="blue"),
                    ),
                    spacing="3"
                ),
                value="login"
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("Nombre de usuario", "Ingrese su usuario", "text", "username"),
                        form_fields("Correo Electrónico", "Ingrese su correo electrónico", "email", "email"),
                        form_fields("Contraseña", "Ingrese su contraseña", "password", "password"),
                        form_fields("Confirmar Contraseña", "Confirme su contraseña", "password", "confirm_password"),
                        rx.button("Registrarse", type="submit", color_scheme="blue"),
                    ),
                    spacing="3"
                ),
                value="signup"
            ),
            background=["gray.800"],\
            padding="20px",
            border_radius="5px",
            box_shadow="rgba(0,0,0,0.25) 0px 3px 8px",
            margin= "auto",
            margin_top="1--px",
            width="400px",
        )
    )

def form_fields(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.form.label(label),
        rx.input(
            placeholder=placeholder,
            type=type,
            name=name,
            # on_focus=LoginState.clear_error,  # "LoginState" is not defined
        ),
        align_items="flex-start",
        width="100%",
    )
