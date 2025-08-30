import reflex as rx
import random


# Backend
class State(rx.State):
    data: list[dict] = [
        {"month": "January", "yrib": 500, "xron": 800, "kabl": 300, "fret": 900, "skir": 200},
        {"month": "February", "yrib": 600, "xron": 700, "kabl": 400, "fret": 900, "skir": 400},
        {"month": "March", "yrib": 700, "xron": 600, "kabl": 500, "fret": 600, "skir": 500},
        {"month": "April", "yrib": 800, "xron": 500, "kabl": 600, "fret": 800, "skir": 1100},
    ]
    @rx.event
    def xron_data(self):
        for item in self.data:
            print(f"Xron resources used in \t{item['month']} 2025 \t➡️\t{item['xron']} units")
        print("")
        yield rx.toast.success(f"XRON {item['month']} 2025 → {item['xron']} units")

            
    @rx.event       
    def yrib_data(self):
        for item in self.data:
            print(f"Yrib resources used in \t{item['month']} 2025 \t➡️\t{item['yrib']} units")
        print("")
        yield rx.toast.success(f"YRIB {item['month']} 2025 → {item['yrib']} units")

    @rx.event       
    def skir_data(self):
        for item in self.data:
            print(f"Skir resources used in \t{item['month']} 2025 \t➡️\t{item['skir']} units")
        print("")
        yield rx.toast.success(f"SKIR {item['month']} 2025 → {item['skir']} units")     
  
    @rx.event
    def kabl_data(self):
        for item in self.data:
            print(f"Kabl resources used in \t{item['month']} 2025 \t➡️\t{item['kabl']} units")
        print()
        yield rx.toast.success(f"KABL {item['month']} 2025 → {item['kabl']} uinits")
  
    @rx.event       
    def fret_data(self):
        for item in self.data:
            print(f"Fret resources used in \t{item['month']} 2025 \t➡️\t{item['fret']} units")
        print("")
        yield rx.toast.success(f"FRET {item['month']} 2025 → {item['fret']} units")
    
    @rx.event
    def new_report(self):
        for dtn in self.data:
            dtn["yrib"] = random.randint(100, 1000)
            dtn["xron"] = random.randint(100, 1000)
            dtn["kabl"] = random.randint(100, 1000)
            dtn["fret"] = random.randint(100, 1000)
            dtn["skir"] = random.randint(100, 1000)
            
# Frontend
@rx.page("/", "Fact and Figures")
def render_chart():
   return rx.center(
       rx.vstack(
           rx.color_mode.button(draggable=True, position="top-right"),
           rx.heading("Resources", font_size="2em", mb="20px", color=rx.color_mode_cond(light="#0202a4ee", dark="#6b6bceee")),
           rx.hstack(
               rx.button("YRIB", on_click=State.yrib_data, background="#e7818178"),
               rx.button("XRON", on_click=State.xron_data, background="#44449b76"),
               rx.button("SKIR", on_click=State.skir_data, background="#55b0fa80"),
               rx.button("KABL", on_click=State.kabl_data, background="#53af2285"), 
               rx.button("FRET", on_click=State.fret_data, background="#ff33aa7a"),
               rx.spacer(),
               rx.button("New Report", background=rx.color_mode_cond(light="#9e9efa", dark="#7e7efa"), on_click=State.new_report, on_mouse_up=rx.toast.info("Report has been generated")),
           ),
           rx.recharts.bar_chart(
               rx.recharts.bar(data_key="yrib", fill="#e7818178", stroke="#e78181"),
               rx.recharts.bar(data_key="xron", fill="#44449b76", stroke="#44449b"),
               rx.recharts.bar(data_key="kabl", fill="#53af2285", stroke="#3f980ff6"),
               rx.recharts.bar(data_key="fret", fill="#ff33aa7a", stroke="#ff33aa"),
               rx.recharts.bar(data_key="skir", fill="#55b0fa80", stroke="#55affa"),
               rx.recharts.x_axis(data_key="month"),
               rx.recharts.y_axis(label=
                    {
                        "value": "Resources",
                        "position": "insideLeft",
                        "angle": -90,
                        "dx": 2,
                        "dy": 30,
                    }
                ),
               rx.recharts.legend(
                    vertical_align="top",  # Place legend above chart
                    align="center",
                    padding="20px",
                ),     
                rx.recharts.cartesian_grid(
                    stroke="#ABB1B4",
                    stroke_dasharray="2 10",  # Dashed grid
                    stroke_opacity=0.1
                ),
                data=State.data,
            ),
            min_height="50vh",
            margin="8vh auto",
            width="90%",
            height=650,
            padding="30px 50px 60px 20px",
            box_shadow=f"0 10px 30px {rx.color_mode_cond(light="rgba(0,0,0,0.2)", dark="rgba(255,255,255,0.4)")}",
            border_radius="12px",
        ),
    )
       

app = rx.App()