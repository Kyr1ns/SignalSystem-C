% Continuous-Time Convolution Integral
t = 0:0.01:5;
dt = t(2) - t(1);

x = ones(size(t));                % x(t) = u(t)
h = exp(-t);                      % h(t) = e^{-t}u(t)

y = zeros(size(t));
for i = 1:length(t)
    tau = 0:dt:t(i);
    xtau = interp1(t, x, tau, 'linear', 0);
    htau = interp1(t, h, t(i) - tau, 'linear', 0);
    y(i) = trapz(tau, xtau .* htau);
end

% Plotting
figure;
subplot(3,1,1); plot(t, x); title('x(t)'); xlabel('t'); ylabel('Amplitude');
subplot(3,1,2); plot(t, h); title('h(t)'); xlabel('t'); ylabel('Amplitude');
subplot(3,1,3); plot(t, y); title('y(t) = x(t) * h(t)'); xlabel('t'); ylabel('Amplitude');
