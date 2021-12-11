from ipykernel.kernelapp import IPKernelApp
from .kernel import MyNodejsKernel
IPKernelApp.launch_instance(kernel_class=MyNodejsKernel)
