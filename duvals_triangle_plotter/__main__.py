from .duvals_triangle_plotter import get_duval_points_traces, get_duvals_triangle_plot

def main():
    # Example usage
    duval_points = [
        get_duval_points_traces([0.09], [0.0], [0.91], "2000-08-16")
    ]

    get_duvals_triangle_plot(duval_points, show_plot=True)

if __name__ == "__main__":
    main()