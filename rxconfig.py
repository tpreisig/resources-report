import reflex as rx

config = rx.Config(
    app_name="resources_report",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)