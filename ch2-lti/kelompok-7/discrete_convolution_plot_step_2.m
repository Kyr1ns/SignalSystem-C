% --- Step-by-Step Discrete Convolution with Calculations ---
% Clear environment
clear; clc; close all;

% 1. DEFINE SIGNALS
% Define index k for the signals
k = -2:10;
% Signal x[k] (e.g., a rectangular pulse)
x = (k >= 0 & k <= 4);
% Signal h[k] (e.g., a decaying ramp)
h = (0.8).^k .* (k >= 0 & k <= 6);

% 2. INITIALIZE FOR CONVOLUTION
% The output signal y[n] will exist from the sum of the starting indices
% to the sum of the ending indices.
n_start = k(1) + k(1);
n_end = k(end) + k(end);
n = n_start:n_end;
y = zeros(1, length(n));

% Flip h[k] to get h[-k] for the convolution process
h_flipped = fliplr(h);
k_flipped = -fliplr(k);

% 3. PERFORM CONVOLUTION STEP-BY-STEP
figure('Name', 'Discrete Convolution Steps', 'Position', [100, 100, 900, 700]);

for i = 1:length(n)
    current_n = n(i);

    % Clear the plot for the new step
    clf;

    % --- Visualization ---
    % Plot original x[k]
    subplot(4, 1, 1);
    stem(k, x, 'b', 'filled', 'LineWidth', 1.5);
    title(['Step ', num2str(i), ' of ', num2str(length(n)), ': Calculating y[', num2str(current_n), ']']);
    ylabel('x[k]');
    grid on;
    xlim([n_start, n_end]);

    % Plot flipped and shifted h[n-k]
    subplot(4, 1, 2);
    % The shifted index for h_flipped is k_flipped + current_n
    stem(k_flipped + current_n, h_flipped, 'r', 'filled', 'LineWidth', 1.5);
    ylabel('h[n-k]');
    grid on;
    xlim([n_start, n_end]);

    % --- Calculation ---
    % Find overlapping indices for multiplication
    [k_common, ix, ih] = intersect(k, k_flipped + current_n);

    % Initialize product array
    product = zeros(1, length(k));
    if ~isempty(k_common)
        % Perform element-wise multiplication on the overlap
        product(ix) = x(ix) .* h_flipped(ih);
    end

    % Calculate the sum to get the convolution result for this n
    y(i) = sum(product);

    % --- More Visualization ---
    % Plot the product x[k]h[n-k]
    subplot(4, 1, 3);
    stem(k, product, 'g', 'filled', 'LineWidth', 1.5);
    ylabel('Product');
    grid on;
    xlim([n_start, n_end]);

    % Plot the resulting signal y[n] as it's being built
    subplot(4, 1, 4);
    stem(n, y, 'm', 'filled', 'LineWidth', 1.5);

    % --- Display Calculation on Plot ---
    % Create the string showing the summation
    non_zero_elements = product(product ~= 0);
    if isempty(non_zero_elements)
        sum_str = '0';
    else
        % Create a string like "0.8 + 0.64 + ..."
        sum_str = strjoin(arrayfun(@(val) sprintf('%.2f', val), non_zero_elements, 'UniformOutput', false), ' + ');
    end
    calc_title = sprintf('y[%d] = sum(Product) = %s = %.2f', current_n, sum_str, y(i));
    title(calc_title);

    ylabel('y[n]');
    xlabel('n');
    grid on;
    xlim([n_start, n_end]);

    % Pause to allow viewing of the current step
    pause(1.5);
end

% Display final result in the command window
disp('Final convolved signal y[n]:');
disp(y);
