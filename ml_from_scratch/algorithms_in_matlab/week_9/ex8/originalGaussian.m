function p = originalGaussian(X, mu, Sigma2)
%
%p(x)=p(x1;mu1,sig�1) * p(x2;mu2,sig�2) ... p(xn;mun,sig�n)
%
p =  (1./(sqrt(2 .* pi .* Sigma2))) .* exp(- ((X - mu) .^ 2) ./ (2 * Sigma2));
p = prod(p, 2); %  products of each row
end