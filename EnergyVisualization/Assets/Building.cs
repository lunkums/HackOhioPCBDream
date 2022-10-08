using UnityEngine;

public class Building : MonoBehaviour
{
    [SerializeField] private string _name;

    private Transform building;
    private Material material;

    private void Awake()
    {
        building = transform;
        material = GetComponent<MeshRenderer>().material;
    }

    void Start()
    {
        AdjustBuilding(DataPopulator.Instance.GetData(_name));
    }

    private void AdjustBuilding(float data)
    {
        // Get color before scaling down data
        material.color = DataPopulator.Instance.GetColorFromData(data);
        data /= 1000;
        building.localScale = new Vector3(building.localScale.x, data, building.localScale.z);
        building.position = new Vector3(building.position.x, data / 2, building.position.z);
    }
}
