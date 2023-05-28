#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int K;
int now_height = K - 1;
double distances = 1000005;
vector<double>points;
vector<double>target = {2,4.5};

struct Treenode {
    vector<double>val;
    int height;
    struct Treenode* left;
    struct Treenode* right;
    Treenode(vector<double>_val,int _height) {
        val = _val;
        height = _height;
        left = NULL;
        right = NULL;
    }
};

bool cmp(const vector<double>&a, const vector<double>b) {
    return a[now_height] < b[now_height];
}

Treenode* createKDtree(vector<vector<double>>_data,int deep) {
    int i = 0;
    int j = _data.size() - 1;
    int mid = (i + j + 1) / 2;
    deep = (deep + 1) % K;;
    now_height = deep;
    sort(_data.begin(),_data.end(),cmp);
    Treenode* root = new Treenode(_data[mid],deep);
    if (i < mid) {
        vector<vector<double>>zuo(_data.begin() + i, _data.begin() + mid);
        root->left = createKDtree(zuo, deep);
    }
    if (mid < j) {
        vector<vector<double>>you(_data.begin() + mid + 1, _data.begin() + j + 1);
        root->right = createKDtree(you, deep);
    }
    return root;
}

void middfs(Treenode* node) {
    if (node -> left)
        middfs(node -> left);
    for (int i = 0;i < K;i++)
        cout << node->val[i] << " ";
    cout << endl;
    if (node -> right)
        middfs(node -> right);
}

void midserachmindistance(Treenode* node) {
    if (node -> left)
        midserachmindistance(node->left);
    cout << "当前坐标为:";
    for (int i = 0; i < K; i++)
        cout << node->val[i] << " ";
    cout << endl;
    if (abs(node -> val[node->height] - target[node->height]) > distances)
        return;
    else {
        double temp = 0;
        for (int i = 0; i < K; i++) {
            double r = target[i] - node->val[i];
            temp += r * r;
        }
        if (sqrt(temp) < distances) {
            distances = sqrt(temp);
            points = node -> val;
        }
    }
    if (node->right)
        midserachmindistance(node->right);
}

int main()
{
    vector<vector<double>>data = { {2,3},{5,4},{9,6},{4,7},{8,1},{7,2}};
    K = data[0].size();
    Treenode* root = createKDtree(data,-1);
    middfs(root);
    midserachmindistance(root);
    cout << "目标点为:";
    for (int i = 0; i < K; i++)
        cout << points[i] << " ";
    cout << endl;
    cout << "最小距离为" << distances << endl;
    return 0;
}