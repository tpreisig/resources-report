import reflex as rx
import random

# Backend
class ReportState(rx.State):
  data: list[dict] = []

@rx.event
def report_data(self):
  yield rx.toast.success(f"XRON {item['month']} 2025 → {item['xron']} units")

@rx.event
def new_report(self):
  pass

# Frontend
@rx.event("/", "Facts and Figures")
def render_chart():
  return rx.center(
    rx.vstack(
      rx.color_mode.button(draggable=True, position="top-right"),
      rx.heading("Resources", font_size="2em", mb="20px", color=rx.color_mode_cond(light="#0202a4ee", dark="#6b6bceee")),
    ),
    min_height="50vh",
    margin="8vh auto",
    width="90%",
    height=650,
    padding="30px 50px 60px 20px",
    box_shadow=f"0 10px 30px {rx.color_mode_cond(light="rgba(0,0,0,0.2)", dark="rgba(255,255,255,0.4)")}",
    border_radius="12px",

      
    




