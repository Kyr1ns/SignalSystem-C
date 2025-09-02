% --- Step-by-Step Continuous Convolution (Approximation) with Calculations ---
% Clear environment
clear; clc; close all;

% 1. DEFINE SIGNALS
% Define a fine time-step for approximation
dt = 0.05;
tau = -2:dt:8;

% Signal x(tau) (e.g., a rectangular pulse)
x = (tau >= 0 & tau <= 2);
% Signal h(tau) (e.g., a triangular pulse)
h = tripuls(tau - 1, 2); % Centered at 1, width 2

% 2. INITIALIZE FOR CONVOLUTION
% The output time vector t
t_start = tau(1) + tau(1);
t_end = tau(end) + tau(end);
t = t_start:dt:t_end;
y = zeros(1, length(t));

% Flip h(tau) to get h(-tau)
h_flipped = fliplr(h);
tau_flipped = -fliplr(tau);

% 3. PERFORM CONVOLUTION STEP-BY-STEP
figure('Name', 'Continuous Convolution Steps', 'Position', [100, 100, 900, 700]);

% We will only visualize a subset of steps to speed up the animation
t_visual_indices = 1:5:length(t); % Plot every 5th step

for i = t_visual_indices
    current_t = t(i);

    % Clear the plot for the new step
    clf;

    % --- Visualization ---
    % Plot original x(tau)
    subplot(4, 1, 1);
    plot(tau, x, 'b', 'LineWidth', 1.5);
    title(['Step for t = ', num2str(current_t, '%.2f')]);
    ylabel('x(\tau)');
    grid on;
    ylim([0, 1.2]);
    xlim([t_start, t_end]);

    % Plot flipped and shifted h(t-tau)
    subplot(4, 1, 2);
    plot(tau_flipped + current_t, h_flipped, 'r', 'LineWidth', 1.5);
    ylabel('h(t-\tau)');
    grid on;
    ylim([0, 1.2]);
    xlim([t_start, t_end]);

    % --- Calculation ---
    % Interpolate the shifted signal onto the original tau grid for multiplication
    h_shifted = interp1(tau_flipped + current_t, h_flipped, tau, 'linear', 0);

    % Perform element-wise multiplication
    product = x .* h_shifted;

    % Approximate the integral: sum of the area of rectangles (height * width)
    y(i) = sum(product) * dt;

    % --- More Visualization ---
    % Plot the product x(tau)h(t-tau) and shade the area
    subplot(4, 1, 3);
    area(tau, product, 'FaceColor', 'g', 'EdgeColor', 'g');
    ylabel('Product');
    grid on;
    ylim([0, 1.2]);
    xlim([t_start, t_end]);

    % Plot the resulting signal y(t) as it's being built
    subplot(4, 1, 4);
    plot(t, y, 'm', 'LineWidth', 2);

    % --- Display Calculation on Plot ---
    calc_title = sprintf('y(%.2f) = Area ≈ sum(Product) × dt = %.2f', current_t, y(i));
    title(calc_title);

    ylabel('y(t)');
    xlabel('t');
    grid on;
    xlim([t_start, t_end]);

    % Pause to allow viewing of the current step
    pause(0.01);
end

% For a smooth final plot, calculate all y values (not just visualized ones)
for i = 1:length(t)
    current_t = t(i);
    h_shifted = interp1(tau_flipped + current_t, h_flipped, tau, 'linear', 0);
    product = x .* h_shifted;
    y(i) = sum(product) * dt;
end
% And plot the final, complete result
subplot(4, 1, 4);
plot(t, y, 'm', 'LineWidth', 2);
title('Final Result y(t) = (x*h)(t)');
ylabel('y(t)');
xlabel('t');
grid on;
xlim([t_start, t_end]);
