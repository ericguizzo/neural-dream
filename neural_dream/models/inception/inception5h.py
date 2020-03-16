import torch
import torch.nn as nn
import torch.nn.functional as F
import neural_dream.helper_layers as helper_layers


class Inception5h(nn.Module):

    def __init__(self):
        super(Inception5h, self).__init__()
        self.conv2d0_pre_relu_conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(7, 7), stride=(2, 2), groups=1, bias=True)
        self.conv2d1_pre_relu_conv = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.conv2d2_pre_relu_conv = nn.Conv2d(in_channels=64, out_channels=192, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.mixed3a_1x1_pre_relu_conv = nn.Conv2d(in_channels=192, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3a_3x3_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=192, out_channels=96, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3a_5x5_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=192, out_channels=16, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3a_pool_reduce_pre_relu_conv = nn.Conv2d(in_channels=192, out_channels=32, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3a_3x3_pre_relu_conv = nn.Conv2d(in_channels=96, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.mixed3a_5x5_pre_relu_conv = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(5, 5), stride=(1, 1), groups=1, bias=True)
        self.mixed3b_1x1_pre_relu_conv = nn.Conv2d(in_channels=256, out_channels=128, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3b_3x3_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=256, out_channels=128, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3b_5x5_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=256, out_channels=32, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3b_pool_reduce_pre_relu_conv = nn.Conv2d(in_channels=256, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed3b_3x3_pre_relu_conv = nn.Conv2d(in_channels=128, out_channels=192, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.mixed3b_5x5_pre_relu_conv = nn.Conv2d(in_channels=32, out_channels=96, kernel_size=(5, 5), stride=(1, 1), groups=1, bias=True)
        self.mixed4a_1x1_pre_relu_conv = nn.Conv2d(in_channels=480, out_channels=192, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed4a_3x3_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=480, out_channels=96, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed4a_5x5_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=480, out_channels=16, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed4a_pool_reduce_pre_relu_conv = nn.Conv2d(in_channels=480, out_channels=64, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.mixed4a_3x3_pre_relu_conv = nn.Conv2d(in_channels=96, out_channels=204, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.mixed4a_5x5_pre_relu_conv = nn.Conv2d(in_channels=16, out_channels=48, kernel_size=(5, 5), stride=(1, 1), groups=1, bias=True)
        self.head0_bottleneck_pre_relu_conv = nn.Conv2d(in_channels=508, out_channels=128, kernel_size=(1, 1), stride=(1, 1), groups=1, bias=True)
        self.nn0_pre_relu_matmul = nn.Linear(in_features = 2048, out_features = 1024, bias = True)
        self.softmax0_pre_activation_matmul = nn.Linear(in_features = 1024, out_features = 1008, bias = True)


    def add_layers(self):
        self.conv2d0_pre_relu_conv_pad = helper_layers.PadLayer()
        self.maxpool0_pad = helper_layers.PadLayer()
        self.conv2d2_pre_relu_conv_pad = helper_layers.PadLayer()
        self.maxpool1_pad = helper_layers.PadLayer()
        self.mixed3a_pool_pad = helper_layers.PadLayer()
        self.mixed3a_3x3_pre_relu_conv_pad = helper_layers.PadLayer()
        self.mixed3a_5x5_pre_relu_conv_pad = helper_layers.PadLayer()
        self.mixed3b_pool_pad = helper_layers.PadLayer()
        self.mixed3b_3x3_pre_relu_conv_pad = helper_layers.PadLayer()
        self.mixed3b_5x5_pre_relu_conv_pad = helper_layers.PadLayer()
        self.maxpool4_pad = helper_layers.PadLayer()
        self.mixed4a_pool_pad = helper_layers.PadLayer()
        self.mixed4a_3x3_pre_relu_conv_pad = helper_layers.PadLayer()
        self.mixed4a_5x5_pre_relu_conv_pad = helper_layers.PadLayer()

        self.conv2d0 = helper_layers.ReluLayer()
        self.conv2d1 = helper_layers.ReluLayer()
        self.conv2d2 = helper_layers.ReluLayer()
        self.mixed3a_1x1 = helper_layers.ReluLayer()
        self.mixed3a_3x3_bottleneck = helper_layers.ReluLayer()
        self.mixed3a_5x5_bottleneck = helper_layers.ReluLayer()
        self.mixed3a_pool_reduce = helper_layers.ReluLayer()
        self.mixed3a_3x3 = helper_layers.ReluLayer()
        self.mixed3a_5x5 = helper_layers.ReluLayer()
        self.mixed3b_1x1 = helper_layers.ReluLayer()
        self.mixed3b_3x3_bottleneck = helper_layers.ReluLayer()
        self.mixed3b_5x5_bottleneck = helper_layers.ReluLayer()
        self.mixed3b_pool_reduce = helper_layers.ReluLayer()
        self.mixed3b_3x3 = helper_layers.ReluLayer()
        self.mixed3b_5x5 = helper_layers.ReluLayer()
        self.mixed4a_1x1 = helper_layers.ReluLayer()
        self.mixed4a_3x3_bottleneck = helper_layers.ReluLayer()
        self.mixed4a_5x5_bottleneck = helper_layers.ReluLayer()
        self.mixed4a_pool_reduce = helper_layers.ReluLayer()
        self.mixed4a_3x3 = helper_layers.ReluLayer()
        self.mixed4a_5x5 = helper_layers.ReluLayer()
        self.head0_bottleneck = helper_layers.ReluLayer()
        self.nn0 = helper_layers.ReluLayer()

        self.maxpool0 = helper_layers.MaxPool2dLayer()
        self.maxpool1 = helper_layers.MaxPool2dLayer()
        self.mixed3a_pool = helper_layers.MaxPool2dLayer()
        self.mixed3b_pool = helper_layers.MaxPool2dLayer()
        self.maxpool4 = helper_layers.MaxPool2dLayer()
        self.mixed4a_pool = helper_layers.MaxPool2dLayer()

        self.localresponsenorm0 = helper_layers.LocalResponseNormLayer()
        self.localresponsenorm1 = helper_layers.LocalResponseNormLayer()

        self.mixed3a = helper_layers.CatLayer()
        self.mixed3b = helper_layers.CatLayer()
        self.mixed4a = helper_layers.CatLayer()

        self.softmax0 = helper_layers.SoftMaxLayer()


    def forward(self, x):
        conv2d0_pre_relu_conv_pad = self.conv2d0_pre_relu_conv_pad(x, (2, 3, 2, 3))
        conv2d0_pre_relu_conv = self.conv2d0_pre_relu_conv(conv2d0_pre_relu_conv_pad)
        conv2d0         = self.conv2d0(conv2d0_pre_relu_conv)
        maxpool0_pad    = self.maxpool0_pad(conv2d0, (0, 1, 0, 1), value=float('-inf'))
        maxpool0        = self.maxpool0(maxpool0_pad, kernel_size=(3, 3), stride=(2, 2), padding=0, ceil_mode=False)
        localresponsenorm0 = self.localresponsenorm0(maxpool0, size=9, alpha=9.999999747378752e-05, beta=0.5, k=1)
        conv2d1_pre_relu_conv = self.conv2d1_pre_relu_conv(localresponsenorm0)
        conv2d1         = self.conv2d1(conv2d1_pre_relu_conv)
        conv2d2_pre_relu_conv_pad = self.conv2d2_pre_relu_conv_pad(conv2d1, (1, 1, 1, 1))
        conv2d2_pre_relu_conv = self.conv2d2_pre_relu_conv(conv2d2_pre_relu_conv_pad)
        conv2d2         = self.conv2d2(conv2d2_pre_relu_conv)
        localresponsenorm1 = self.localresponsenorm1(conv2d2, size=9, alpha=9.999999747378752e-05, beta=0.5, k=1)
        maxpool1_pad    = self.maxpool1_pad(localresponsenorm1, (0, 1, 0, 1), value=float('-inf'))
        maxpool1        = self.maxpool1(maxpool1_pad, kernel_size=(3, 3), stride=(2, 2), padding=0, ceil_mode=False)
        mixed3a_1x1_pre_relu_conv = self.mixed3a_1x1_pre_relu_conv(maxpool1)
        mixed3a_3x3_bottleneck_pre_relu_conv = self.mixed3a_3x3_bottleneck_pre_relu_conv(maxpool1)
        mixed3a_5x5_bottleneck_pre_relu_conv = self.mixed3a_5x5_bottleneck_pre_relu_conv(maxpool1)
        mixed3a_pool_pad = self.mixed3a_pool_pad(maxpool1, (1, 1, 1, 1), value=float('-inf'))
        mixed3a_pool    = self.mixed3a_pool(mixed3a_pool_pad, kernel_size=(3, 3), stride=(1, 1), padding=0, ceil_mode=False)
        mixed3a_1x1     = self.mixed3a_1x1(mixed3a_1x1_pre_relu_conv)
        mixed3a_3x3_bottleneck = self.mixed3a_3x3_bottleneck(mixed3a_3x3_bottleneck_pre_relu_conv)
        mixed3a_5x5_bottleneck = self.mixed3a_5x5_bottleneck(mixed3a_5x5_bottleneck_pre_relu_conv)
        mixed3a_pool_reduce_pre_relu_conv = self.mixed3a_pool_reduce_pre_relu_conv(mixed3a_pool)
        mixed3a_3x3_pre_relu_conv_pad = self.mixed3a_3x3_pre_relu_conv_pad(mixed3a_3x3_bottleneck, (1, 1, 1, 1))
        mixed3a_3x3_pre_relu_conv = self.mixed3a_3x3_pre_relu_conv(mixed3a_3x3_pre_relu_conv_pad)
        mixed3a_5x5_pre_relu_conv_pad = self.mixed3a_5x5_pre_relu_conv_pad(mixed3a_5x5_bottleneck, (2, 2, 2, 2))
        mixed3a_5x5_pre_relu_conv = self.mixed3a_5x5_pre_relu_conv(mixed3a_5x5_pre_relu_conv_pad)
        mixed3a_pool_reduce = self.mixed3a_pool_reduce(mixed3a_pool_reduce_pre_relu_conv)
        mixed3a_3x3     = self.mixed3a_3x3(mixed3a_3x3_pre_relu_conv)
        mixed3a_5x5     = self.mixed3a_5x5(mixed3a_5x5_pre_relu_conv)
        mixed3a         = self.mixed3a((mixed3a_1x1, mixed3a_3x3, mixed3a_5x5, mixed3a_pool_reduce), 1)
        mixed3b_1x1_pre_relu_conv = self.mixed3b_1x1_pre_relu_conv(mixed3a)
        mixed3b_3x3_bottleneck_pre_relu_conv = self.mixed3b_3x3_bottleneck_pre_relu_conv(mixed3a)
        mixed3b_5x5_bottleneck_pre_relu_conv = self.mixed3b_5x5_bottleneck_pre_relu_conv(mixed3a)
        mixed3b_pool_pad = self.mixed3b_pool_pad(mixed3a, (1, 1, 1, 1), value=float('-inf'))
        mixed3b_pool    = self.mixed3b_pool(mixed3b_pool_pad, kernel_size=(3, 3), stride=(1, 1), padding=0, ceil_mode=False)
        mixed3b_1x1     = self.mixed3b_1x1(mixed3b_1x1_pre_relu_conv)
        mixed3b_3x3_bottleneck = self.mixed3b_3x3_bottleneck(mixed3b_3x3_bottleneck_pre_relu_conv)
        mixed3b_5x5_bottleneck = self.mixed3b_5x5_bottleneck(mixed3b_5x5_bottleneck_pre_relu_conv)
        mixed3b_pool_reduce_pre_relu_conv = self.mixed3b_pool_reduce_pre_relu_conv(mixed3b_pool)
        mixed3b_3x3_pre_relu_conv_pad = self.mixed3b_3x3_pre_relu_conv_pad(mixed3b_3x3_bottleneck, (1, 1, 1, 1))
        mixed3b_3x3_pre_relu_conv = self.mixed3b_3x3_pre_relu_conv(mixed3b_3x3_pre_relu_conv_pad)
        mixed3b_5x5_pre_relu_conv_pad = self.mixed3b_5x5_pre_relu_conv_pad(mixed3b_5x5_bottleneck, (2, 2, 2, 2))
        mixed3b_5x5_pre_relu_conv = self.mixed3b_5x5_pre_relu_conv(mixed3b_5x5_pre_relu_conv_pad)
        mixed3b_pool_reduce = self.mixed3b_pool_reduce(mixed3b_pool_reduce_pre_relu_conv)
        mixed3b_3x3     = self.mixed3b_3x3(mixed3b_3x3_pre_relu_conv)
        mixed3b_5x5     = self.mixed3b_5x5(mixed3b_5x5_pre_relu_conv)
        mixed3b         = self.mixed3b((mixed3b_1x1, mixed3b_3x3, mixed3b_5x5, mixed3b_pool_reduce), 1)
        maxpool4_pad    = self.maxpool4_pad(mixed3b, (0, 1, 0, 1), value=float('-inf'))
        maxpool4        = self.maxpool4(maxpool4_pad, kernel_size=(3, 3), stride=(2, 2), padding=0, ceil_mode=False)
        mixed4a_1x1_pre_relu_conv = self.mixed4a_1x1_pre_relu_conv(maxpool4)
        mixed4a_3x3_bottleneck_pre_relu_conv = self.mixed4a_3x3_bottleneck_pre_relu_conv(maxpool4)
        mixed4a_5x5_bottleneck_pre_relu_conv = self.mixed4a_5x5_bottleneck_pre_relu_conv(maxpool4)
        mixed4a_pool_pad = self.mixed4a_pool_pad(maxpool4, (1, 1, 1, 1), value=float('-inf'))
        mixed4a_pool    = self.mixed4a_pool(mixed4a_pool_pad, kernel_size=(3, 3), stride=(1, 1), padding=0, ceil_mode=False)
        mixed4a_1x1     = self.mixed4a_1x1(mixed4a_1x1_pre_relu_conv)
        mixed4a_3x3_bottleneck = self.mixed4a_3x3_bottleneck(mixed4a_3x3_bottleneck_pre_relu_conv)
        mixed4a_5x5_bottleneck = self.mixed4a_5x5_bottleneck(mixed4a_5x5_bottleneck_pre_relu_conv)
        mixed4a_pool_reduce_pre_relu_conv = self.mixed4a_pool_reduce_pre_relu_conv(mixed4a_pool)
        mixed4a_3x3_pre_relu_conv_pad = self.mixed4a_3x3_pre_relu_conv_pad(mixed4a_3x3_bottleneck, (1, 1, 1, 1))
        mixed4a_3x3_pre_relu_conv = self.mixed4a_3x3_pre_relu_conv(mixed4a_3x3_pre_relu_conv_pad)
        mixed4a_5x5_pre_relu_conv_pad = self.mixed4a_5x5_pre_relu_conv_pad(mixed4a_5x5_bottleneck, (2, 2, 2, 2))
        mixed4a_5x5_pre_relu_conv = self.mixed4a_5x5_pre_relu_conv(mixed4a_5x5_pre_relu_conv_pad)
        mixed4a_pool_reduce = self.mixed4a_pool_reduce(mixed4a_pool_reduce_pre_relu_conv)
        mixed4a_3x3     = self.mixed4a_3x3(mixed4a_3x3_pre_relu_conv)
        mixed4a_5x5     = self.mixed4a_5x5(mixed4a_5x5_pre_relu_conv)
        mixed4a         = self.mixed4a((mixed4a_1x1, mixed4a_3x3, mixed4a_5x5, mixed4a_pool_reduce), 1)
        head0_pool      = F.avg_pool2d(mixed4a, kernel_size=(5, 5), stride=(3, 3), padding=(0,), ceil_mode=False, count_include_pad=False)
        head0_bottleneck_pre_relu_conv = self.head0_bottleneck_pre_relu_conv(head0_pool)
        head0_bottleneck = self.head0_bottleneck(head0_bottleneck_pre_relu_conv)
        avgpool_2d = nn.AdaptiveAvgPool2d((4, 4))
        x = avgpool_2d(head0_bottleneck)
        x = torch.flatten(x, 1)
        nn0_pre_relu_matmul = self.nn0_pre_relu_matmul(x)
        nn0             = self.nn0(nn0_pre_relu_matmul)
        nn0_reshape     = torch.reshape(input = nn0, shape = (-1,1024))
        softmax0_pre_activation_matmul = self.softmax0_pre_activation_matmul(nn0_reshape)
        softmax0        = self.softmax0(softmax0_pre_activation_matmul)
        return softmax0