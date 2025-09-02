% Continuous-Time Convolution Visualization
t = 0:0.01:5;
dt = t(2) - t(1);
x = ones(size(t));               % x(t) = u(t)
h = exp(-t);                     % h(t) = e^{-t}u(t)

figure;
for tau_idx = 1:20:length(t)
    tau = t(tau_idx);
    h_shifted = interp1(t, h, tau - t, 'linear', 0);  % Flip & shift
    product = x .* h_shifted;
    y_tau = trapz(t, product);                        % Integrate

    clf;
    subplot(3,1,1); plot(t, x); title('x(t)'); ylim([0 1.2]);
    subplot(3,1,2); plot(t, h_shifted); title(['h(tau - t), tau = ' num2str(tau)]); ylim([0 1.2]);
    subplot(3,1,3); plot(t, product); title(['x(t) * h(tau - t), ∫ = ' num2str(y_tau)]); ylim([0 1.2]);

    pause(0.5);  % Animate each step
end
