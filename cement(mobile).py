from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

# Color scheme
BACKGROUND_COLOR = get_color_from_hex("#242121")  # Dark background
PRIMARY_COLOR = get_color_from_hex("#09192E")  # Dark primary color
ACCENT_COLOR = get_color_from_hex("#64B5F6")  # Light blue accent
TEXT_COLOR = get_color_from_hex("#f5f5f5")  # Light text color
INPUT_COLOR = get_color_from_hex("#060708")  # Input text color
beton_karisimlari = {
    "C5": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 160, "Su": 200, "Kum": 900, "Çakıl": 1100},
            "CEM 2": {"Çimento": 150, "Su": 195, "Kum": 920, "Çakıl": 1080},
            "CEM 3": {"Çimento": 155, "Su": 198, "Kum": 910, "Çakıl": 1090},
        }
    },
    "C10": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 200, "Su": 190, "Kum": 850, "Çakıl": 1150},
            "CEM 2": {"Çimento": 190, "Su": 185, "Kum": 870, "Çakıl": 1130},
            "CEM 3": {"Çimento": 195, "Su": 188, "Kum": 860, "Çakıl": 1140},
        }
    },
    "C15": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 230, "Su": 180, "Kum": 820, "Çakıl": 1180},
            "CEM 2": {"Çimento": 220, "Su": 175, "Kum": 840, "Çakıl": 1160},
            "CEM 3": {"Çimento": 225, "Su": 178, "Kum": 830, "Çakıl": 1170},
        }
    },
    "C20": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 300, "Su": 180, "Kum": 800, "Çakıl": 1200},
            "CEM 2": {"Çimento": 280, "Su": 175, "Kum": 820, "Çakıl": 1180},
            "CEM 3": {"Çimento": 290, "Su": 178, "Kum": 810, "Çakıl": 1190},
        }
    },
    "C25": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 340, "Su": 175, "Kum": 780, "Çakıl": 1220},
            "CEM 2": {"Çimento": 320, "Su": 170, "Kum": 800, "Çakıl": 1200},
            "CEM 3": {"Çimento": 330, "Su": 173, "Kum": 790, "Çakıl": 1210},
        }
    },
    "C30": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 380, "Su": 170, "Kum": 760, "Çakıl": 1240},
            "CEM 2": {"Çimento": 360, "Su": 165, "Kum": 780, "Çakıl": 1220},
            "CEM 3": {"Çimento": 370, "Su": 168, "Kum": 770, "Çakıl": 1230},
        }
    },
    "C35": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 420, "Su": 165, "Kum": 740, "Çakıl": 1260},
            "CEM 2": {"Çimento": 400, "Su": 160, "Kum": 760, "Çakıl": 1240},
            "CEM 3": {"Çimento": 410, "Su": 163, "Kum": 750, "Çakıl": 1250},
        }
    },
    "C40": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 450, "Su": 160, "Kum": 720, "Çakıl": 1280},
            "CEM 2": {"Çimento": 430, "Su": 155, "Kum": 740, "Çakıl": 1260},
            "CEM 3": {"Çimento": 440, "Su": 158, "Kum": 730, "Çakıl": 1270},
        }
    },
    "C45": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 470, "Su": 155, "Kum": 710, "Çakıl": 1290},
            "CEM 2": {"Çimento": 450, "Su": 150, "Kum": 730, "Çakıl": 1270},
            "CEM 3": {"Çimento": 460, "Su": 153, "Kum": 720, "Çakıl": 1280},
        }
    },
    "C50": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 490, "Su": 150, "Kum": 700, "Çakıl": 1300},
            "CEM 2": {"Çimento": 470, "Su": 145, "Kum": 720, "Çakıl": 1280},
            "CEM 3": {"Çimento": 480, "Su": 148, "Kum": 710, "Çakıl": 1290},
        }
    },
    "C55": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 510, "Su": 145, "Kum": 690, "Çakıl": 1310},
            "CEM 2": {"Çimento": 490, "Su": 140, "Kum": 710, "Çakıl": 1290},
            "CEM 3": {"Çimento": 500, "Su": 143, "Kum": 700, "Çakıl": 1300},
        }
    },
    "C60": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 530, "Su": 140, "Kum": 680, "Çakıl": 1320},
            "CEM 2": {"Çimento": 510, "Su": 135, "Kum": 700, "Çakıl": 1300},
            "CEM 3": {"Çimento": 520, "Su": 138, "Kum": 690, "Çakıl": 1310},
        }
    },
    "C65": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 550, "Su": 135, "Kum": 670, "Çakıl": 1330},
            "CEM 2": {"Çimento": 530, "Su": 130, "Kum": 690, "Çakıl": 1310},
            "CEM 3": {"Çimento": 540, "Su": 133, "Kum": 680, "Çakıl": 1320},
        }
    },
    "C70": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 570, "Su": 130, "Kum": 660, "Çakıl": 1340},
            "CEM 2": {"Çimento": 550, "Su": 125, "Kum": 680, "Çakıl": 1320},
            "CEM 3": {"Çimento": 560, "Su": 128, "Kum": 670, "Çakıl": 1330},
        }
    },
    "C75": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 590, "Su": 125, "Kum": 650, "Çakıl": 1350},
            "CEM 2": {"Çimento": 570, "Su": 120, "Kum": 670, "Çakıl": 1330},
            "CEM 3": {"Çimento": 580, "Su": 123, "Kum": 660, "Çakıl": 1340},
        }
    },
    "C80": {
        "Karışım Oranları": {
            "CEM 1": {"Çimento": 610, "Su": 120, "Kum": 640, "Çakıl": 1360},
            "CEM 2": {"Çimento": 590, "Su": 115, "Kum": 660, "Çakıl": 1340},
            "CEM 3": {"Çimento": 600, "Su": 118, "Kum": 650, "Çakıl": 1350},
        }
    }
}


class ConcreteApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # Main layout with padding and spacing
        layout = BoxLayout(orientation='vertical', padding=[20, 15, 20, 15], spacing=10)

        # Setting the background color
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        # ScrollView to ensure content fits on smaller screens
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_layout = GridLayout(cols=1, padding=10, spacing=15, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        # Widgets with increased sizes and text sizes for mobile
        self.concrete_spinner = self.create_spinner('Beton Türünü Seçiniz', [key for key in beton_karisimlari.keys()])
        self.cement_spinner = self.create_spinner('Çimento Türünü Seçiniz', [])
        self.amount_input = self.create_amount_input()
        calc_button = self.create_calculate_button()

        # Add widgets to the scroll layout
        scroll_layout.add_widget(self.concrete_spinner)
        scroll_layout.add_widget(self.cement_spinner)
        scroll_layout.add_widget(self.amount_input)
        scroll_layout.add_widget(calc_button)

        # Add scroll layout to the scroll view
        scroll_view.add_widget(scroll_layout)

        # Add the scroll view to the main layout
        layout.add_widget(scroll_view)

        # Add the main layout to the root widget
        root.add_widget(layout)

        return root

    def create_spinner(self, initial_text, values):
        """Create a Spinner widget optimized for mobile."""
        spinner = Spinner(
            text=initial_text,
            values=values,
            size_hint=(1, None),  # Full width, fixed height
            height=120,  # Height increased for mobile
            font_size='20sp',  # Font size increased for mobile
            background_color=PRIMARY_COLOR,
            color=TEXT_COLOR
        )
        spinner.bind(text=self.update_cement_spinner)
        return spinner

    def create_amount_input(self):
        """Create a TextInput widget for entering the concrete amount."""
        input_widget = TextInput(
            hint_text='Gerekli m³ Miktarını Giriniz',
            size_hint=(1, None),  # Full width, fixed height
            height=120,  # Height increased for mobile
            font_size='20sp',  # Font size increased for mobile
            background_color=TEXT_COLOR,
            foreground_color=INPUT_COLOR
        )
        input_widget.bind(focus=self.on_focus)
        return input_widget

    def create_calculate_button(self):
        """Create a Button widget to calculate the concrete mix."""
        button = Button(
            text='Hesapla',
            size_hint=(1, None),  # Full width, fixed height
            height=120,  # Height increased for mobile
            font_size='20sp',  # Font size increased for mobile
            background_color=ACCENT_COLOR,
            color=TEXT_COLOR
        )
        button.bind(on_press=self.calculate_mixture)
        return button

    def update_cement_spinner(self, spinner, text):
        """Update the cement spinner options based on the selected concrete type."""
        selected_concrete = spinner.text
        if selected_concrete in beton_karisimlari:
            cement_types = list(beton_karisimlari[selected_concrete]["Karışım Oranları"].keys())
            self.cement_spinner.values = cement_types

    def calculate_mixture(self, instance):
        """Calculate and display the mixture based on the selected values."""
        # Get selected values
        concrete_type = self.concrete_spinner.text
        cement_type = self.cement_spinner.text
        amount = self.amount_input.text

        if amount == 'Gerekli m³ Miktarını Giriniz' or not amount:
            self.show_error_popup("Lütfen miktar alanını doldurun.")
            return

        amount = float(amount)
        if concrete_type in beton_karisimlari:
            if cement_type in beton_karisimlari[concrete_type]["Karışım Oranları"]:
                mix = beton_karisimlari[concrete_type]["Karışım Oranları"][cement_type]
                result = {ingredient: amount * quantity for ingredient, quantity in mix.items()}
                self.show_result_popup(result)
            else:
                self.show_error_popup("Çimento türü bulunamadı.")
        else:
            self.show_error_popup("Beton türü bulunamadı.")

    def show_result_popup(self, result):
        """Display the calculated mixture results in a popup."""
        content = BoxLayout(orientation='vertical', padding=10)
        for ingredient, quantity in result.items():
            content.add_widget(Label(text=f"{ingredient}: {quantity:.2f} kg", font_size='18sp', color=TEXT_COLOR))

        popup = Popup(
            title='Karışım Sonuçları',
            content=content,
            size_hint=(0.8, 0.8)  # Adjust popup size to fit on mobile screens
        )
        popup.open()

    def show_error_popup(self, message):
        """Display an error message in a popup."""
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message, font_size='18sp', color=TEXT_COLOR))

        popup = Popup(
            title='Hata',
            content=content,
            size_hint=(0.8, 0.4)  # Adjust popup size to fit on mobile screens
        )
        popup.open()

    def on_focus(self, instance, value):
        """Handle the focus event for the TextInput."""
        if value:
            if instance.text == 'Gerekli m³ Miktarını Giriniz':
                instance.text = ''
                instance.foreground_color = (0, 0, 0, 1)  # Change text color to black
        else:
            if not instance.text:
                instance.text = 'Gerekli m³ Miktarını Giriniz'
                instance.foreground_color = (0.5, 0.5, 0.5, 1)  # Change text color to gray

    def _update_rect(self, instance, value):
        """Update the rectangle size and position when the layout changes."""
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    ConcreteApp().run()