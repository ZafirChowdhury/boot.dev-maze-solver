from graphics import Window, Point, Line

def main():
    window = Window()

    line = Line(Point(50, 50), Point(400, 400))
    window.draw_line(line)

    window.wait_for_close()


if __name__ == "__main__":
    main()
